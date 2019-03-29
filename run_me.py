#!/usr/bin/env python3

import optparse

parser = optparse.OptionParser()

parser.add_option('-d', '--dry-run',
    action="store", dest="dry-run",
    help="Perform dry-run", default=True)

(options, args) = parser.parse_args()

