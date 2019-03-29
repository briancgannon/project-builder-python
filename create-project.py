#!/usr/bin/env python3

import optparse

parser = optparse.OptionParser()

parser.add_option("-d", "--dry-run",
    action="store", dest="dry-run",
    help="Perform dry-run", default=False)

parser.add_option("-t", "--token",
    action="store", dest="token",
    help="Input ADO Personal Access Token", default="ProvidePersonalAccessToken")

parser.add_option("-o", "--organization",
    action="store", dest="organization",
    help="Input ADO organization")


(options, args) = parser.parse_args()


