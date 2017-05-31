#!/usr/bin/env python
from __future__ import print_function

import os

HIERARCHY = {
    'root': [
        'notes',
        'scratch',
    ],
    'work': [
        'todo',
        'ideas',
        'goals',
        'concerns',
        'relationships',
    ],
    'personal': [
        'books',
        'todo',
        'ideas',
        'goals',
        'concerns',
        'relationships',
    ],
}


def get_full_path(*args):
    base_dir = os.path.join(os.path.expanduser('~'), 'notes')
    if args:
        return os.path.join(base_dir, os.path.join(*args))
    return base_dir


def make_file(filename, directories):
    path = get_full_path(*([d for d in directories] + ['%s.md' % filename]))
    if os.path.exists(path):
        return
    make_directory(directories)
    with open(path, 'w+') as f:
        f.write('# %s' % filename.capitalize())
        print('Creating file %s' % path)


def make_directory(directories):
    path = get_full_path(*directories)
    if os.path.exists(path):
        return
    os.makedirs(path)
    print('Creating directory %s' % path)


def make_recursive(tree, directories=None):
    if directories is None:
        directories = []
    for dir_name, dir_contents in tree.iteritems():
        if dir_name == 'root':
            if not isinstance(dir_contents, list):
                raise Exception('Root directory should be a list of files')
            for filename in dir_contents:
                make_file(filename, directories)
        elif isinstance(dir_contents, dict):
            make_recursive(dir_contents, directories + [dir_name])
        elif isinstance(dir_contents, list):
            for filename in dir_contents:
                make_file(filename, directories + [dir_name])
        elif isinstance(dir_contents, basestring):
            make_file(dir_contents, directories + [dir_name])
        else:
            raise Exception('Invalid directory contents')


if __name__ == '__main__':
    make_recursive(HIERARCHY)
    print('Done!')
