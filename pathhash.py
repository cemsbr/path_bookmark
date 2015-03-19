import os.path
import json
import os
import sys
import re
from shlex import quote


class PathHash:
    USE_KEY = 'use_count'
    PATH_KEY = 'path'

    def __init__(self, db_file):
        self._phs = {}
        self._db_file = db_file
        self._load_db()

    def exec(self, args):
        rx = re.compile(r'=([^/]+)(/.*)?')
        cmd = []
        for arg in args:
            match = rx.match(arg)
            expanded = self._expand_arg(arg, match)
            cmd.append(expanded)
        return ' '.join(cmd)

    def _expand_arg(self, arg, match):
        if match and match.group(1) in self._phs:
            alias, suffix = match.groups()
            ph = self._phs[alias]
            path = ph[PathHash.PATH_KEY]
            if suffix:
                expanded = path + suffix
            else:
                expanded = path
            self._update_use_count(ph)
        else:
            expanded = arg
        return quote(expanded)

    def _update_use_count(self, ph):
        ph[PathHash.USE_KEY] += 1
        self.save()

    def _load_db(self):
        if os.path.exists(self._db_file):
            with open(self._db_file) as f:
                self._phs = json.load(f)

    def save(self):
        # TODO enforce 600 permission (eval security)
        with open(self._db_file, 'w') as f:
            json.dump(self._phs, f, sort_keys=True, indent=2)

    def ls(self):
        alpha_sorted = sorted(self._phs)  # stable sorting

        def get_use_count(alias):
            return self._phs[alias][PathHash.USE_KEY]

        for alias in sorted(alpha_sorted, key=get_use_count, reverse=True):
            path = self._phs[alias][PathHash.PATH_KEY]
            print('{}: {}'.format(alias, path))

    def add(self, alias, path):
        self._phs[alias] = {PathHash.PATH_KEY: path, PathHash.USE_KEY: 0}

    def rm(self, aliases):
        for alias in aliases:
            try:
                del self._phs[alias]
            except KeyError:
                print('alias {} not found.'.format(alias), file=sys.stderr)

    def keys(self):
        # Bash will always sort these keys!
        return self._phs.keys()
