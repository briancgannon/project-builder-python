#!/usr/bin/env python3

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import json
import os
import requests

organization_url = 'https://dev.azure.com/gannonbrian'
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
my_project_name = "test-project"

# ADO stuff
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
core_client = connection.clients.get_core_client()

def create_project(name):
    core_client.queue_create_project(project_to_create=name)

create_project(my_project_name)
