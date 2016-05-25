Path Bookmark
=============

Tired of typing long paths or managing lots of symlinks? Try this little
hackable hack!
- Increase productivity with only a few intuitive commands
- Few lines of python 3 and bash code
- All data is saved in a json file

There's no package to install it, neither tests to run, but installing is easy
and the code is short. Usage and installation instruction follows.

## Usage

### Easy help
```p``` for help and path list:
```
PathBookmark Help
=================
(omitted)

Paths saved
===========
(omitted)
```

### Path management
- ```pa``` adds an alias for a directory or updates it:
```bash
~$ cd /path/to/my/long/project/directory
# Use current dir when not specified:
directory$ pa project
# The full version:
directory$ pa downloads /a/folder/different/from/the/current/one
```

- ```pl``` lists the added directories, most used first, then alphabetically:
```bash
directory$ pl
downloads: /a/folder/different/from/the/current/one
project: /path/to/my/long/project/directory
```

- ```pr``` removes an alias:
```bash
directory$ pr downloads  # (tab completion)
directory$ pl
project: /path/to/my/long/project/directory
```

### Using path aliases
- ```pe``` can run any command by evaluating aliases prefixed with ```=```:
```bash
~$ pe ls =project  # (tab completion)
PathBookmark: ls /path/to/my/long/project/directory
LICENSE  my_paths.json  PathBookmark.py  pb.py  pb.sh  README.md
```

- ```pcd``` is a shortcut to change dir (equivalent to ```pe cd```):
```bash
~$ pcd =project  # (tab completion)
PathBookmark: cd /path/to/my/long/project/directory
directory$
```

## Installation

1. Clone this repo or download its contents to ```~/.path_bookmark```
1. Add to your ```~/.bashrc```:
```. ~/.path_bookmark/pb.sh```
