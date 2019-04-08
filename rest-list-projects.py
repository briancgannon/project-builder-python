#!/usr/bin/env python3

import os
import requests

# Config
organizational_url = 'https://dev.azure.com/gannonbrian'
projects_url = organizational_url + '/_apis/projects?api-version=5.0'
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
my_project_name = "test-project"
my_project_description = "Test Project Description"
project_params = {'name':my_project_name}

resp = requests.get(url = projects_url)
if resp.status_code !=200:
    raise Exception('GET /projects/ {}'.format(resp.status_code))
for project in resp.json():
    print('{} {} {}'.format(project['id'], project['name'], project['description']))
