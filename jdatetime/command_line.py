#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Julian Date.

Usage:
  jdate
  jdate +format
  jdate (-h | --help)

  Options:
  -h --help     Show this screen.

"""

import sys
from jdatetime import jdatetime


def main():
    args = sys.argv[1:]
    if not args:
        print "{:%a %b %m %H:%M:%S %Y}".format(jdatetime.now())
        return
    for i in args:
        if i in ('-h', '--help'):
            print __doc__
            return
        if i.startswith('+'):
            print jdatetime.now().__format__(i[1:])
            return
    print __doc__


if __name__ == '__main__':
    main()
