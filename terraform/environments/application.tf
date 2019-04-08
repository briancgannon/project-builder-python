module "production_application" {
  source                     = "../../modules/aws/application"
  env_name                   = "production"
  database_engine            = "PostgreSQL"
  database_engine_version    = "10.4"
  database_allocated_storage = 250
  database_name              = ""
  database_snapshot_name     = ""  
}
