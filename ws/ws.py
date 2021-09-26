from driver import Driver
from pathlib import Path
from pprint import pprint as pp
from pdb import set_trace as trace
import re
from shutil import copytree
import shlex

from tools import *

class Workshop(Driver):
    def process_file(self, p):
        super().process_file(p)

    # def run(self):
    #     super().run()
        # print('Hello world')
        # self.cmdloop()

    def do_new(self, args):
        print("Creating a new project...")
        args = shlex.split(args)
        old_dir = Path.cwd()
        cd(copytree(self.settings['template'], args[0], symlinks=True,
                    ignore=lambda s, ls: ['.git', '.venv']))
        PROJECT_NAME = args[0].split('-')[0]
        FILES_2_EDIT = ['README.md', 'etc/hw.conf', 'hw/configure.py',
                        'hw/__init__.py', 'hw/__main__.py']
        for p in [Path(s) for s in FILES_2_EDIT]:
            p.write_text(re.sub('hw', PROJECT_NAME, p.read_text()))
        CODE_2_CHANGE = ['hw/hw.py', 'hw/__main__.py']
        for p in [Path(s) for s in CODE_2_CHANGE]:
            p.write_text(re.sub('HelloWorld', args[1], p.read_text()))
        Path('hw/hw.py').rename(f'hw/{PROJECT_NAME}.py')
        Path('etc/hw.conf').rename(f'etc/{PROJECT_NAME}.conf')
        Path('hw').rename(PROJECT_NAME)
        cd(old_dir)
