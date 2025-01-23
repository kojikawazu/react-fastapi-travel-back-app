# ---------------------------------------------
# IAM role
# ---------------------------------------------
resource "google_cloud_run_service_iam_member" "invoker" {
  service  = google_cloud_run_service.fast_travel_app_service.name
  location = var.gcp_region
  project  = var.gcp_project_id

  role   = var.invoker_role
  member = var.invoker_member
}
