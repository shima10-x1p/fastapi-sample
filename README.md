# FastAPI-Sample

OpenAPI Generatorで自動生成されたFastAPIコードにおける、アーキテクチャ検討のためのサンプルです。

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


## 独自箇所
main.pyに一部手動実装を入れてます。
```python
class TraceMiddleware(BaseHTTPMiddleware):
    """
    リクエストからX-Trace-IDを取得し、ロガーに設定するミドルウェア(ここだけ手動)
    """
    async def dispatch(self, request: Request, call_next):
        # リクエストからX-Trace-IDを取得
        trace_id = request.headers.get('X-Trace-ID')
        
        # X-Trace-IDがない場合は新規生成
        if not trace_id:
            trace_id = str(uuid.uuid4())
            
        # ロガーにTrace IDを設定
        logger = get_logger()
        logger.set_trace_id(trace_id)
        
        # リクエスト処理を実行
        response = await call_next(request)
        
        # レスポンスヘッダーにTrace IDを追加
        response.headers['X-Trace-ID'] = trace_id
        
        return response
```
