""" Define a class that parses simple configuration files. """

from configparser import ConfigParser
import logging
from os import environ, sep
from pathlib import Path
from warnings import warn

from globals import BASEDIR
from tools import Logging

class Configure(dict):
    """ Same thing as a `ConfigParser`, but simpler. """

    CONFIG_FILE = BASEDIR / ('etc' + sep + 'hw.conf')

    DEFAULT = """[DEFAULT]
# Uncomment this line to send `logging` messages to a file.
# logfile = log/hw.log
"""

    def __init__(self, file=None):
        """ Parse the file and store the values.

            :file: Configuration file to be parsed.
                   (default is `None`, in which case `DEFAULT` is used.)
        """

        # print(f'{args=}\n{bool(args)=}\n{kwargs=}')
        super().__init__(self)
        # print("Reading configuration file...")
        try:
            if not file: file = self.CONFIG_FILE
            # self.log = logging.getLogger(__name__)
            parser = ConfigParser()
            parser.read_string('[DEFAULT]\n' + Path(file).read_text())
            self |= parser['DEFAULT']
        except FileNotFoundError:
            parser.read_string(self.DEFAULT)
        except TypeError:
            warn("Support for Python 3.8 will be phased out in due course.")
            self.update(parser['DEFAULT'])
