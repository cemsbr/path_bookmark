#!/usr/bin/env python3
import sys
from pathhash import PathHash
import os
import os.path


def help_msg():
    return "PathHash Help\n" \
           "=============\n" \
           "Use aliases instead of full paths. Usage:\n" \
           "- ha my_alias: my_alias will point to current path\n" \
           "- ha my_alias path: my_alias will point to specified path\n" \
           "- hl: list current aliases and their paths\n" \
           "- hcd =my_alias: change to my_alias\'s path" \
           " (TAB to autocomplete)\n" \
           '- he: run what follows, replacing "=my_alias" by its path\n' \
           "- hr my_alias my_alias2 ...: remove alias(es)\n"


if __name__ == '__main__':
    ph = PathHash(os.path.expanduser('~/.path_hash/my_paths.json'))

    if len(sys.argv) < 2:
        print(help_msg())
        # TODO if has path
        print('Paths Saved')
        print('===========')
        ph.ls()
        sys.exit(0)

    cmd = sys.argv[1]

    # TODO expand relative path
    if cmd == 'add' and len(sys.argv) > 2:
        key = sys.argv[2]
        path = sys.argv[3] if len(sys.argv) > 3 else os.getcwd()
        ph.add(key, path)
        ph.save()
    elif cmd == 'ls':
        ph.ls()
    elif cmd == 'rm' and len(sys.argv) > 2:
        keys = sys.argv[2:]
        ph.rm(keys)
        ph.save()
    elif cmd == 'exec':
        sh = ph.exec(sys.argv[2:])
        # TODO escape
        print("echo 'PathHash: {}'; {}".format(sh, sh))
    elif cmd == 'keys':
        print(' '.join(ph.keys()))
    else:
        print(help_msg())
