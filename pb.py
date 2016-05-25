#!/usr/bin/env python3
import os
import sys
from pathbookmark import PathBookmark


def help_msg():
    return """PathBookmark Help
=================
Use bookmark names instead of full paths. Usage:
- pa my_alias: my_alias will point to current path
- pa my_alias path: my_alias will point to specified path
- pl: list current aliases and their paths
- pcd =my_alias: change to my_alias\'s path (TAB to autocomplete)
- pe: run what follows, replacing "=my_alias" by its path
- pr my_alias my_alias2 ...: remove alias(es)"""


if __name__ == '__main__':
    pb = PathBookmark(os.path.expanduser('~/.path_bookmark/my_paths.json'))

    if len(sys.argv) < 2:
        print(help_msg())
        print('\nPaths Saved')
        print('===========')
        pb.ls()
        sys.exit(0)

    cmd = sys.argv[1]

    # TODO expand relative path
    if cmd == 'add' and len(sys.argv) > 2:
        key = sys.argv[2]
        path = sys.argv[3] if len(sys.argv) > 3 else os.getcwd()
        pb.add(key, path)
        pb.save()
    elif cmd == 'ls':
        pb.ls()
    elif cmd == 'rm' and len(sys.argv) > 2:
        keys = sys.argv[2:]
        pb.rm(keys)
        pb.save()
    elif cmd == 'replace':
        sh = pb.replace(sys.argv[2:])
        # TODO escape
        print("echo 'PathBookmark: {}'; {}".format(sh, sh))
    elif cmd == 'keys':
        print(' '.join(pb.keys()))
    else:
        print(help_msg())
