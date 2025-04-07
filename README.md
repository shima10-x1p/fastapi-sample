# FastAPI-Sample

このPythonパッケージは[OpenAPI Generator](https://openapi-generator.tech)プロジェクトによって自動生成されています:

- API バージョン: 1.0.0
- ジェネレーターバージョン: 7.13.0-SNAPSHOT
- ビルドパッケージ: org.openapitools.codegen.languages.PythonFastAPIServerCodegen

## 必要条件

Python >= 3.7

## インストールと使用方法

サーバーを実行するには、ルートディレクトリから以下のコマンドを実行してください:

```bash
pip3 install -r requirements.txt
PYTHONPATH=src uvicorn openapi_server.main:app --host 0.0.0.0 --port 8080
```

ブラウザで `http://localhost:8080/docs/` にアクセスすると、APIドキュメントが表示されます。

## Dockerでの実行

Dockerコンテナでサーバーを実行するには、ルートディレクトリから以下のコマンドを実行してください:

```bash
docker-compose up --build
```

## テスト

テストを実行するには:

```bash
pip3 install pytest
PYTHONPATH=src pytest tests
```
