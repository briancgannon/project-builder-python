#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint
import os

# ADO -> User -> Security -> Create Personal Access Token
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
organization_url = 'https://dev.azure.com/developertown'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

core_client = connection.clients.get_core_client()
projects = core_client.get_projects()

# Show details about each project in the console
for project in projects:
    pprint.pprint(project.__dict__)
