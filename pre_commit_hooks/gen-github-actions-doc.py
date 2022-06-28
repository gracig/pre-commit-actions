from __future__ import annotations

import argparse
import re
from typing import Sequence

from pre_commit_hooks.check_yaml import yaml

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('workflow_file', nargs='1', help='Filenames to check.')
    args = parser.parse_args(argv)
    retval = 0
    try:
        with open(args.workflow_file, encoding='UTF-8') as f:
            actions = yaml.load(f)
            readme=""
            with open("README.md", 'r') as f:
                readme = f.read().decode('utf8')
            pattern = re.compile(r"""<!--BEGIN DOC-->.*<!--END DOC>""",re.MULTILINE)
            if pattern.match(readme):
                readme = pattern.sub("<!--BEGIN DOC-->\nSecond Text\n<!--END DOC-->", readme)            
            else:
                readme = readme + "<!--BEGIN DOC-->\nFirst Text\n<!--END DOC-->"            
            with open("README.md", 'w') as f:
                f.write(readme.encode("utf-8"))

    except yaml.YAMLError as exc:
        print(exc)
        retval = 1
    except:
        retval = 1

    return retval

if __name__ == '__main__':
    raise SystemExit(main())
