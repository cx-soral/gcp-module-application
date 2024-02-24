module "gcp_module_application" {
  source = "../../modules/gcp-module-application"

  landscape_file = "../../../config/landscape.yaml"
  applications_file = "../../../config/applications.yaml"
}
