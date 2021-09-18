"""Run the program."""

from pprint import pp
import sys

from driver import Driver
from ws import Workshop

if __name__ == '__main__':
    if {'-t', '--testing'}.intersection(sys.argv):
        Driver().run()
    else:
        Workshop().run()
