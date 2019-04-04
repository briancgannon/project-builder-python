#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import os

organization_url = 'https://dev.azure.com/gannonbrian'
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
my_project_name = "test-project"

# ADO stuff
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

def get_project_names():
    core_client = connection.clients.get_core_client()
    return (project.name for project in core_client.get_projects())

def check_project_name_availability(name):
    projects = get_project_names()
    project_name = ""
    for p in projects:
        if p == name:
            print("Current projects: " + p)
            project_name = input("Project name already in use. Please choose a different name: ")
            return project_name

def create_ado_project(name):
    core_client = connection.clients.get_core_client()
    core_client.queue_create_project(name)

project_name = check_project_name_availability(my_project_name)
create_ado_project(project_name)
