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

def create_ado_project(id, name, description):
    core_client = connection.clients.get_core_client()
    core_client.queue_create_project(abbreviation="MTP",
        description="Test Project",
        name="test-project",
        id="tp-01",
        capabilities={'process-template':'agile',
            'version-control':'git'}
            )

# TODO: Until create status = wellFormed
resp = requests.get('https://dev.azure.com/gannonbrian/_apis/operations/tp-01/?api-version=5.0')
create_ado_project(my_project_id, my_project_name, my_project_description)

