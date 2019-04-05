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
