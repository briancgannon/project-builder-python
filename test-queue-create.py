#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import json
import os
import requests

organization_url = 'https://dev.azure.com/gannonbrian'
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
my_project_name = "default-project"
my_project_description = "This is garbage."

# ADO stuff
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
core_client = connection.clients.get_core_client()

def create_project(name, description):
    core_client.queue_create_project(name=name,
        description=description,
        capabilities={'process-template':'agile',
            'version-control':'git'}
        )

# Get project ID and check for creation status
def get_project_id(name):
    projects = core_client.get_projects()
    for project in projects:
        if name == project.name:
            project_name_found = True
            return project.id
        else:
            project_name_found = False

    if project_name_found == False:
        raise ValueError("ERROR: Project name not found in current projects.")

def get_project_state(project_id):
    projects = core_client.get_projects()
    for project in projects:
        if project_id == project.id:
            project_id_found = True
            return project.state
        else:
            project_id_found = False

    if project_id_found == False:
        raise ValueError("ERROR: Unable to return project state from current projects.")

my_id = get_project_id(my_project_name)
my_status = get_project_state(my_id)

# wait until project creation is complete
while True:
    my_status = get_project_state(my_id)
    if my_status == 'wellFormed':
        break
