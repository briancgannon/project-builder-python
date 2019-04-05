#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint
import optparse
import os

# Org
organization_url = 'https://dev.azure.com/gannonbrian'
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')

# Create a connection
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client
core_client = connection.clients.get_core_client()

# Get a list of the projects in the org
projects = core_client.get_projects()

# Show projects
for project in projects:
    pprint.pprint(project.__dict__)
    print("")
    print("Here is ID:")
    print(project.id)

