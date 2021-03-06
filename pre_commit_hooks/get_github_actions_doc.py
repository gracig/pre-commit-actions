from __future__ import annotations

import argparse
import re
import io
from typing import Sequence
import ruamel.yaml
yaml = ruamel.yaml.YAML(typ='safe')


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)
    retval = 0
    filename = ".github/workflows/main.yaml"
    print("FILENAME: ", filename)
    try:
        with open(filename, encoding='UTF-8') as f:
            actions = yaml.load(f)
        buf = io.BytesIO()
        yaml.dump(actions, buf)
        doc_string = str(buf,'UTF-8')
        readme=open('README.md', encoding='UTF-8').read()
        pattern = re.compile(r"(.*?)<!--BEGIN_DOC-->.*<!--END_DOC-->(.*)", flags=(re.DOTALL | re.MULTILINE))
        if pattern.match(readme):
            readme = pattern.sub("\\1<!--BEGIN_DOC-->\n{}\n<!--END_DOC-->\\2".format(doc_string), readme)
        else:
            print("Did not find doc")
            readme = "{}\n<!--BEGIN_DOC-->\n{}\n<!--END_DOC-->\n".format(readme, doc_string)
        open("README.md", 'wb').write(readme.encode("utf-8"))

    except Exception as exc:
        print("EXCEPTION HAS OCCURRED: ", exc)
        retval = 1

    return retval

if __name__ == '__main__':
    raise SystemExit(main())
