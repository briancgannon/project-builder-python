#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from msrest.serialization import Model
import json
import os
import requests
import logging

# Logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Config
organization_url = 'https://dev.azure.com/gannonbrian'
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
project_name = "test-project"

# TODO: Fix this
project_params = {'name': project_name}

# Azure Devops connection
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
core_client = connection.clients.get_core_client()

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

def create_project(project):
        project = core_client.queue_create_project(project)

try:
    # TODO: Fix this
    create_project(project_params)
except Exception as error:
    logger.exception(error)

new_project_id = get_project_id(project_name)
new_project_status = get_project_state(new_project_id)

# wait until project creation is complete
while True:
    my_status = get_project_state(new_project_id)
    if my_status == 'wellFormed':
        break


