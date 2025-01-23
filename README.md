# 遠征関係のWebアプリケーション(バックエンド WebAPI側)

## Summary

- 遠征時の費用を管理したい。
- まずはバックエンドWebAPI側を作成する。

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3.11-009688?style=for-the-badge&logo=Python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Supabase](https://img.shields.io/badge/Supabase-009688?style=for-the-badge&logo=Supabase&logoColor=white)](https://supabase.com/)
[![Google Cloud Run](https://img.shields.io/badge/Google_Cloud_Run-4285F4?style=for-the-badge&logo=Google-Cloud&logoColor=white)](https://cloud.google.com/run)
[![Google Cloud Artifact Registry](https://img.shields.io/badge/Google_Cloud_Artifact_Registry-4285F4?style=for-the-badge&logo=Google-Cloud&logoColor=white)](https://cloud.google.com/artifact-registry)
[![Google Cloud Run](https://img.shields.io/badge/Google_Cloud_Run-4285F4?style=for-the-badge&logo=Google-Cloud&logoColor=white)](https://cloud.google.com/run)

## 開発環境の実行(ローカル)

```bash
# 仮想環境の作成
python3 -m venv venv
# 仮想環境の有効化
source venv/bin/activate
# パッケージのインストール
pip install -r requirements.txt
# アプリケーションの起動
cd app
uvicorn main:app --reload
```

## 開発環境の実行(コンテナ)

```bash
docker-compose up -d
```

## 開発環境の動作確認

curlコマンドやPostmanなどでAPIを実行してみる。

```bash
# [例]デバッグ用のAPI
http://localhost:8000/debug
```

# Other

TODO

