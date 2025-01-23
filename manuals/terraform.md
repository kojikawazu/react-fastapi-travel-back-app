# セットアップ

## Google Cloud のセットアップ

```bash
# 認証情報の設定
gcloud auth application-default login

# プロジェクト設定
gcloud config set project [project-id]

# プロジェクト取得
gcloud config get-value project
```

## Artifact Registryへデプロイ

```bash
# Artifact Registry API を有効化
gcloud services enable artifactregistry.googleapis.com

# ビルド
docker build -t asia-northeast1-docker.pkg.dev/[project-id]/[repository-id]/[image-name] .

# テスト
docker run -p 8000:8000 asia-northeast1-docker.pkg.dev/[project-id]/[repository-id]/[image-name]

# (上手くいかない場合のデバッグ用)
docker run -it --rm asia-northeast1-docker.pkg.dev/[project-id]/[repository-id]/[image-name] bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# 認証
gcloud auth configure-docker asia-northeast1-docker.pkg.dev

# プッシュ
docker push asia-northeast1-docker.pkg.dev/[project-id]/[repository-id]/[image-name]

# リスト
gcloud artifacts docker images list asia-northeast1-docker.pkg.dev/[project-id]/[repository-id]
```

## Terraform のセットアップ

```bash
# ディレクトリ移動
cd terraform

# 初期化
terraform init

# 計画
terraform plan

# 適用
terraform apply -auto-approve
```
