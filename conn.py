#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint
import optparse

# Get PAT from user input
parser = optparse.OptionParser()

parser.add_option('-t', '--token',
    action="store", dest="token",
    help="token string", default="DefaultPersonalAccessToken")

parser.add_option('-o', '--organization',
    action="store", dest="organization",
    help="organization string", default="DefaultAzureDevopsOrganizationg")


options, args = parser.parse_args()

# Require PAT
if not options.token:
    parser.error('Please provide your Azure DevOps Personal Access Token')

elif not options.organization:
    parser.error('Please provide the target Azure DevOps Organization')

print('Token: ', options.token)
print('Organization: ', options.organization)



# Fill in with your personal access token and org URL
personal_access_token = 'token-token'
organization_url = 'https://dev.azure.com/gannonbrian'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()

# Get the list of projects in the org
projects = core_client.get_projects()

# Show details about each project in the console
for project in projects:
    pprint.pprint(project.__dict__)
