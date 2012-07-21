"""

    yamltools -- command line interface to process YAML
    ===================================================

"""

import os
import sys
import yaml

__all__ = ()

def error(msg, code=1):
    print >> sys.stderr, 'error: %s' % msg
    sys.exit(code)

def bykey(data, key):
    for p in key.split('.'):
        data = data[p]
    return data

class Loader(yaml.BaseLoader):

    def construct_undefined(self, node):
        return self.construct_scalar(node)

def load(stream):
    loader = Loader(stream)
    try:
        return loader.get_single_data()
    finally:
        loader.dispose()

def main():
    args = sys.argv[1:]

    if not args:
        error('provide command: get, set')
    cmd = args.pop(0)
    if not cmd in ('get', 'set'):
        error('unknown command %s' % cmd)

    if not args:
        error('provide YAML filename')
    filename = args.pop(0)
    if not os.path.exists(filename):
        error('%s does not exist' % filename)
    with open(filename, 'r') as fd:
        data = load(fd)

    if cmd == 'get':
        if not args:
            error('provide key to get data from')
        key = args.pop(0)
        try:
            print bykey(data, key)
        except KeyError:
            error('key %s does not exist' % key)
    elif cmd == 'set':
        error('not implemented')
