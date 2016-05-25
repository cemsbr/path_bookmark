import json
import os
import sys
import re
from shlex import quote


class PathBookmark:
    USE_KEY = 'usage'
    PATH_KEY = 'path'

    def __init__(self, db_file):
        self._pbs = {}
        self._db_file = db_file
        self._load_db()

    def replace(self, args):
        rx = re.compile(r'=([^/]+)(/.*)?')
        cmd = []
        for arg in args:
            match = rx.match(arg)
            expanded = self._expand_arg(arg, match)
            cmd.append(expanded)
        return ' '.join(cmd)

    def _expand_arg(self, arg, match):
        if match and match.group(1) in self._pbs:
            alias, suffix = match.groups()
            pb = self._pbs[alias]
            path = pb[PathBookmark.PATH_KEY]
            if suffix:
                expanded = path + suffix
            else:
                expanded = path
            self._update_use_count(pb)
        else:
            expanded = arg
        return quote(expanded)

    def _update_use_count(self, pb):
        pb[PathBookmark.USE_KEY] += 1
        self.save()

    def _load_db(self):
        if os.path.exists(self._db_file):
            with open(self._db_file) as f:
                self._pbs = json.load(f)

    def save(self):
        # TODO enforce 600 permission (security)
        with open(self._db_file, 'w') as f:
            json.dump(self._pbs, f, sort_keys=True, indent=2)

    def ls(self):
        alpha_sorted = sorted(self._pbs)  # stable sorting

        def get_use_count(alias):
            return self._pbs[alias][PathBookmark.USE_KEY]

        for alias in sorted(alpha_sorted, key=get_use_count, reverse=True):
            path = self._pbs[alias][PathBookmark.PATH_KEY]
            print('{}: {}'.format(alias, path))

    def add(self, alias, path):
        self._pbs[alias] = {PathBookmark.PATH_KEY: path,
                            PathBookmark.USE_KEY: 0}

    def rm(self, aliases):
        for alias in aliases:
            try:
                del self._pbs[alias]
            except KeyError:
                print('alias {} not found.'.format(alias), file=sys.stderr)

    def keys(self):
        # Bash will always sort these keys!
        return self._pbs.keys()
