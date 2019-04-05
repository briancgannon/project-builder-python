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

if not options.token:
    parser.error('Please provide an Azure DevOps Personal Access Token')
elif not options.organization:
    parser.error('Please provide an Azure DevOps Organization')

if options.organization:
    organization_url = 'https://dev.azure.com/' + options.organization
else:
    organization_url = 'https://dev.azure.com/'

# Create a connection
credentials = BasicAuthentication('', options.token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client
core_client = connection.clients.get_core_client()

# Get a list of the projects in the org
projects = core_client.get_projects()

# Show projects
for project in projects:
    pprint.pprint(project.__dict__)

