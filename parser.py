#!/usr/bin/env python3

import optparse

parser = optparse.OptionParser()

parser.add_option('-t', '--token',
    action="store", dest="token",
    help="token string", default="DefaultTokenString")

(options, args) = parser.parse_args()

# Require PAT
if not options.token:
    parser.error('Please provide your Azure DevOps Personal Access Token')

print('Token: ', options.token)
