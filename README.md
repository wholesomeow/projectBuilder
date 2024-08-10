# Table of Contents
- [Purpose](#purpose)
- [Usage](#usage)
- [Basic File Structure](#basic-file-structure)
- [Install](#install)
- [Creating Custom Structures](#creating-custom-structures)

# Purpose
This python project is intended to be a CLI tool that creates a standardized file structure for coding projects in my common languages.
This project can build standard structures in the following languages:
- [x] Python
- [ ] Go
- [ ] C++
- [ ] Bash

In addition to building out the file structure, it also includes simple default/reference files.
These files will provide a stubbed out starting point with minimal boiler plate.
The reference files include some simple syntax and functions in case I forget how to code.

# Usage
The following shows the help output of this command, which shows its intended usage:

```
usage: sbuild.py [--new [TARGET] | --remove [TARGET] | --archive [TARGET] | --update [TARGET]] [-a] [-r] [-v] [-h]

TARGET will always be the file path to the directory, with the default being the current location

description:

sbuild is a CLI Tool that automates the creation, removal, and archival of full file structures in my common coding languages.
Using this will ensure that all projects starts in a standardized and version controlled way.

examples:

sbuild -r
sbuild --new example_project
sbuild --new example_project -a -v
sbuild --remove ../example_project

options:
  -h, --help          show this help message and exit
  --new [TARGET]      | Creates new project structure at target directory
  --remove [TARGET]   | Removes existing project at target directory
  --archive [TARGET]  | Marks project at target directory "archived" and places in gitignore
  --update [TARGET]   | Updates target directory structure to new reference structure (Use with care: May break code)
  -a, --advanced      | Advanced project structure; Will override default option of "basic" structure
  -r, --release       | Gives release version information
  -v, --verbose       | Presents more output to the command-line for troubleshooting
```

# Basic File Structure
The basic file structure will generally follow a similar outline:
```
ROOT/
├─ package_management.file
├─ source_files/
│  ├─ stubLib.source
│  ├─ stubClass.source
│  ├─ stubExecutable.source
├─ project_name/
│  ├─ library_files/
│  │  ├─ stubLib.source
├─ data/
├─ docs/
│  ├─ reference.md
├─ tests/
│  ├─ stubTest.source
├─ README.md
```

This will obviously change for each language and language implementation, but the general purpose will remain true to the example above.
For projects that do not require source files, library files, and header files to exist or be seperated, their basic implementations will omit the library_files directory and instead combine source and library files together.
Advanced implementations for those same languages may utilize a C-like project structure for the sake of homogony across the repository.
Further research will be needed.

# Install
I have no idea how to package stuff for install.
But I guess I'll figure it out.

# Creating Custom Structures
Some standard reference json files are included on install, but in the event that a custom structure or updated structure is desired there is a template json.
Duplicate this configuration, rename, and populate with desired structure.