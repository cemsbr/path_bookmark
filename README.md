Path Hash
=========

Tired of typing long paths or managing lots of symlinks? Try this little
hackable hack!
- Increase productivity with only a few intuitive commands
- Few lines of python 3 and bash code
- All data is saved in a json file

There's no package to install it, neither tests to run, but installing is easy
and the code is short. Usage and installation instruction follows.

## Usage

### Easy help
```h``` for help and path list:
```
PathHash Help
=============
(omitted)

Paths saved
===========
(omitted)
```

### Path management
- ```ha``` adds an alias for a directory or updates it:
```bash
~$ cd /path/to/my/long/project/directory
# Use current dir when not specified:
directory$ ha project
# The full version:
directory$ ha downloads /a/folder/different/from/the/current/one
```

- ```hl``` lists the added directories, most used first, then alphabetically:
```bash
directory$ hl
downloads: /a/folder/different/from/the/current/one
project: /path/to/my/long/project/directory
```

- ```hr``` removes an alias:
```bash
directory$ hr downloads  # (tab completion)
directory$ hl
project: /path/to/my/long/project/directory
```

### Using path aliases
- ```he``` can run any command by evaluating aliases prefixed with ```=```:
```bash
~$ he ls =project  # (tab completion)
PathHash: ls /path/to/my/long/project/directory
LICENSE  my_paths.json  pathhash.py  ph.py  ph.sh  README.md
```

- ```hcd``` is a shortcut to change dir (equivalent to ```he cd```):
```bash
~$ hcd =project  # (tab completion)
PathHash: cd /path/to/my/long/project/directory
directory$
```

## Installation

1. Clone this repo or download its contents to ```~/.path_hash```
1. Add to your ```~/.bashrc```:
```. ~/.path_hash/ph.sh```
