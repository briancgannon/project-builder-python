# DevOps Project Builder
Internal DevOps tool for automated deploy of new development projects and resources in the DT Azure Devops org.

## Scope
- Azure Devops (ADO)
    - New Project
        - Boards, Repo, Process Template (Agile/Scrum)
        - Default generic pipeline defintions for common tech stacks (default: react + asp.net core + postgres)
        - Service Connections
- Terraform (TF)
    - Clones and init's default POC infrastructure repo for desired platform (AWS, GCE)

### Requirements
- ADO account in DT Org with Project creation/edit perms
- API/CLI authentication
    - Use ENV VAR (default):  `export $AZURE_DEVOPS_PAT="youreazuredevopspersonalaccesstoken"`
- API Client Libraries:  https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-5.0#client-libraries

#### Project Config
- See `default-project-config.json` in project root dir
- 

#### Project Create
- REQUIRED: name
- OPTIONAL: abbreviation, description
- https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects/create?view=azure-devops-rest-5.0


