import os
import subprocess
import argparse
import textwrap

from dataclasses import dataclass

import directoryCreatorLib
import flightLib


def parseArgs():
  parser = argparse.ArgumentParser(prog='sbuild',
                                   usage='%(prog)s.py [--new [TARGET] | --remove [TARGET] | --archive [TARGET] | --update [TARGET]] [-a] [-r] [-v] [-h]',
                                   formatter_class=argparse.RawDescriptionHelpFormatter,
                                   description=textwrap.dedent('''\
                                      TARGET will always be the file path to the directory, with the default being the current location
                                      
                                      description:
                                      
                                      %(prog)s is a CLI Tool that automates the creation, removal, and archival of full file structures in my common coding languages.
                                      Using this will ensure that all projects starts in a standardized and version controlled way.
                                      
                                      examples:
                                      
                                      %(prog)s -r
                                      %(prog)s --new example_project
                                      %(prog)s --new example_project -a -v
                                      %(prog)s --remove ../example_project
                                      '''))

  # Creating Positional Arguments
  pos_group = parser.add_mutually_exclusive_group()
  pos_group.add_argument('--new',
                         nargs='?',
                         default='.',
                         metavar='TARGET',
                         dest='target',
                         help='| Creates new project structure at target directory')
  
  pos_group.add_argument('--remove',
                         nargs='?',
                         default='.',
                         metavar='TARGET',
                         dest='target',
                         help='| Removes existing project at target directory')

  pos_group.add_argument('--archive',
                         nargs='?',
                         default='.',
                         metavar='TARGET',
                         dest='target',
                         help='| Marks project at target directory "archived" and places in gitignore')

  pos_group.add_argument('--update',
                         nargs='?',
                         default='.',
                         metavar='TARGET',
                         dest='target',
                         help='| Updates target directory structure to new reference structure (Use with care: May break code)')

  # Creating Optional Arguments
  parser.add_argument('-a', '--advanced',
                      action='store_true',
                      help='| Advanced project structure; Will override default option of "basic" structure')
  
  parser.add_argument('-r', '--release',
                      action='store_true',
                      help='| Gives release version information')
  
  parser.add_argument('-v', '--verbose',
                      action='store_true',
                      help='| Presents more output to the command-line for troubleshooting')

  args = parser.parse_args()

  return args


@dataclass
class FlightData:
    current_directory: str
    data_path: str
    target: str
    options: list


def preflight():
  print('Starting Pre-Flight checks')

  # NOTE(wholesomeow): Example subprocess command so I don't have to look up the syntax
  subprocess.run(['python3', '--version'])

  # Get path
  create = directoryCreatorLib
  current_directory = os.getcwd()
  data_path = f'../data/file_structure.json'
  data_target_path = flightLib.validate_directory_symbols(data_path, current_directory)

  print(f'Data Path: {data_path}')

  # Get file structure format - template is the full json config file
  template = create.readFile(data_target_path)
  options = create.readTemplateOptions(template)
  final_path = ''

  data = FlightData(current_directory, data_target_path, final_path, options)

  # TODO(wholesomeow): If any checks fail, exit script and report error

  print('Pre-Flight checks completed')
  print('')

  return data


def postflight(args, preflight_data):
  print('Running Post-Flight checks')

  # TODO(wholesomeow): Check and handle --release or --versbose being passed and exit script

  # TODO(wholesomeow): Check and handle TARGET file path is correct/valid
  current_directory = os.getcwd()

  # Validate Target for relative directory symbols (., ..)
  print('Creating final target path')
  final_path = flightLib.validate_directory_symbols(args.target, current_directory)

  print(f'Current Directory: {current_directory}')
  print(f'Final Path: {final_path}')

  data = FlightData(preflight_data.current_directory, preflight_data.data_path, final_path, preflight_data.options)

  # TODO(wholesomeow): If any checks fail, exit script and report error

  print('Post-Flight checks completed')

  return data


def main(args, postflight_data):
  # TODO(wholesomeow): Re-write the terminal output with textwrap
  print('')
  print('Script Running')

  # Get arguments
  # TODO(wholesomeow): Parse this out to destination path and project name
  print(f'Project Target: {args.target}')

  create = directoryCreatorLib
  template = create.readFile(postflight_data.data_path)
  format = create.getInput(postflight_data.options)

  print('')
  print(f'Building out file structure with format: {format}')

  # Build out directories
  split_root_dir = postflight_data.target.split('/')
  project_name = split_root_dir.pop()
  root_dir = '/'.join(split_root_dir)

  print('')
  structure = template.get(format)

  # Get templates file path
  template_name_arr = []
  template_path = f'../data/templates/'
  split_format = format.split('_')
  for i, v in enumerate(split_format):
    if i == 0:
      template_name_arr.append(v.lower())
    else:
      template_name_arr.append(f'_{v.lower()}')
  template_name = '/'.join(template_name_arr)
  selected_template = f'{template_path}{template_name}'
  template_dir = flightLib.validate_directory_symbols(selected_template, preflight_data.current_directory)
  print(f'Selected Template: {template_dir}')

  create.createDir(root_dir, project_name)
  create.parseFormat(postflight_data.target, structure, template_dir)

  print('')
  print('Script Finished')


if __name__ == '__main__':
  args = parseArgs()
  preflight_data = preflight()
  postflight_data = postflight(args, preflight_data)
  main(args, postflight_data)