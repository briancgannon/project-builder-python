#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import optparse

# Options
parser = optparse.OptionParser()

parser.add_option("-t", "--token",
    action="store", dest="token",
    help="ADO Personal Access Token")

(options, args) = parser.parse_args()

bg_org = 'https://dev.azure.com/gannonbrian'
bg_project = "bgannon-test"

if not options.token:
    parser.error('Please provide an Azure DevOps Personal Access Token.')

# Connection & client
credentials = BasicAuthentication('', options.token)
connection = Connection(base_url=bg_org, creds=credentials)

def get_projects():
    core_client = connection.clients.get_core_client()
    return (project.name for project in core_client.get_projects())

current_projects = get_projects()

for cp in current_projects:
    print(cp)
