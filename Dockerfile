# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存パッケージをコピー
COPY ./requirements.txt .
COPY ./app/.env .
# 必要なファイルをコピー
COPY ./app /app

# パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# 環境変数を設定してPythonが作業ディレクトリを認識できるようにする
ENV PYTHONPATH=/app

# サーバーを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
