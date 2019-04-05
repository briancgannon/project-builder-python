#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import json
import os
import requests

organization_url = 'https://dev.azure.com/gannonbrian'
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
my_project_id = "test-01"
my_project_name = "test-project"
my_project_description = "This is garbage."

# ADO stuff
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
core_client = connection.clients.get_core_client()

def create_ado_project(id, name, description):
    core_client.queue_create_project(abbreviation="MTP",
        description="Test Project",
        name="test-project",
        id="tp-01",
        capabilities={'process-template':'agile',
            'version-control':'git'}
            )

# Get project ID and check for creation status
def get_project_id(name):
    projects = core_client.get_projects()
    for project in projects:
        if name == project.name:
            return project.id

def get_project_status(project_id):
    projects = core_client.get_projects()
    for project in projects:
        if project_id == project.id:
            return project.status

my_id = get_project_id(my_project_name)
my_status = get_project_status(my_id)

