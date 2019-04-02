#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint
import optparse

parser = optparse.OptionParser()

parser.add_option("-t", "--token",
    action="store", dest="token",
    help="ADO Personal Access Token")

parser.add_option("-o", "--organization",
    action="store", dest="organization",
    help="ADO organization")

(options, args) = parser.parse_args()

