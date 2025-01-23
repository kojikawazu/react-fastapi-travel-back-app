# ---------------------------------------------
# Artifact Registry
# ---------------------------------------------
# Artifact Registryリポジトリの作成
resource "google_artifact_registry_repository" "fast_travel_app_repo" {
  location      = var.gcp_region
  repository_id = var.repository_id
  description   = "Docker repository for Fast Travel App"
  format        = "DOCKER"
}

# GCR API の有効化
resource "google_project_service" "artifact_registry_api" {
  service = "artifactregistry.googleapis.com"
}
