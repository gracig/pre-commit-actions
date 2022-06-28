from __future__ import annotations

import argparse
import re
from typing import Sequence

from pre_commit_hooks.check_yaml import yaml

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)
    retval = 0
    for filename in args.filenames:
        print("FILENAME: ", filename)
        try:
            with open(filename, encoding='UTF-8') as f:
                actions = yaml.load(f)

            readme=open('README.md', encoding='UTF-8').read()
            pattern = re.compile("BEGIN DOC.*END DOC", flags=re.DOTALL | re.MULTILINE)
            if pattern.match(readme):
                readme = pattern.sub("\nBEGIN DOC\nSecond Text\nEND DOC\n", readme)            
            else:
                readme = readme + "\nBEGIN DOC\nFirst Text\nEND DOC\n"            
            open("README.md", 'wb').write(readme.encode("utf-8"))

        except Exception as exc:
            print(exc)
            retval = 1


        return retval

if __name__ == '__main__':
    raise SystemExit(main())
