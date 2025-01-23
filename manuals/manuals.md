# Python + FastAPIの環境構築

## 仮想環境の構築

```bash
python3 -m venv venv
```

## 仮想環境を有効化

```bash
source venv/bin/activate
```

## パッケージのインストール

```bash
pip install -r requirements.txt
```

## アプリケーションの起動

```bash
cd app
uvicorn main:app --reload
```
