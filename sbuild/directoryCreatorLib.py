import os
import shutil
import json

def readFile(file_path):
  with open(file_path, 'r') as f:
    data = json.load(f)

  return data


def readTemplateOptions(template):
    option_list = []
    for option in template:
      option_list.append(option)

    return option_list


def getInput(options):
  print(f'File structure template options:')

  count = 1
  for option in options:
    print(f'{count} - {option}')
    count += 1

  selection = str(input('Select file structure option: '))
  format = options[int(selection) - 1]

  return format


def createDir(destination_directory, directory_name):
  path = f'{destination_directory}/{directory_name}'
  print(f'Creating directory at path: {path}')
  try:
    os.makedirs(path, exist_ok=True)
    print(f'Directory {directory_name} created successfully')
  except OSError as error:
    print(f'Directory {directory_name} could not be created')


def copyRenameFile(source_path, destination_path, file_name):
  shutil.copy(f'{source_path}/t_{file_name}', f'{destination_path}/')
  shutil.move(f'{destination_path}/t_{file_name}', f'{destination_path}/{file_name}')


def parseFormat(dir, structure, template_dir):
  for key in structure:
    value = structure.get(key)
    if type(value) is dict:
      parent_dir = key.lower()
      createDir(dir, parent_dir)
      parseFormatSub(f'{dir}/{parent_dir}', value, template_dir)
    else:
      copyRenameFile(template_dir, dir, value)


def parseFormatSub(dir, structure, template_dir):
  for key in structure:
    value = structure.get(key)
    if type(value) is dict:
      createDir(dir, key.lower())
      parseFormatSub(f'{dir}/{key.lower()}', value, template_dir)
    else:
      copyRenameFile(template_dir, dir, value)