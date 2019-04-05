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
my_project_name = "test-project"
my_project_description = "Test Project Description"

# Azure Devops connection
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
core_client = connection.clients.get_core_client()

new_project = ModelProjectInfo(name=my_project_name)

def create_project(project):
    core_client.queue_create_project(project_to_create=project)

try:
    create_project(new_project)
except Exception as error:
    logger.exception(error)
