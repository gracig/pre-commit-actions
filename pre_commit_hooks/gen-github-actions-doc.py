from __future__ import annotations

import argparse
from typing import Sequence

from pre_commit_hooks.check_yaml import yaml

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('workflow_file', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        try:
            with open(filename, encoding='UTF-8') as f:
                actions = yaml.load(f)
                print(actions)
        except yaml.YAMLError as exc:
            print(exc)
            retval = 1
    return retval

if __name__ == '__main__':
    raise SystemExit(main())
