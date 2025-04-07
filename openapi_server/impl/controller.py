import random
from openapi_server.apis.users_api_base import BaseUsersApi
from openapi_server.models.user import User
from openapi_server.logger import get_logger, log_function
from openapi_server.models.get_user_by_id404_response import GetUserById404Response
from fastapi import HTTPException


class Controler(BaseUsersApi):
    """
    APIの実装クラス（コントローラー）
    APIのエンドポイントに対応するメソッドを実装する。
    """
    
    @log_function(level='DEBUG')
    async def create_user(self, user_create, x_trace_id):
        # ロガー取得
        logger = get_logger()
        logger.info(f"ユーザー作成リクエスト: email={user_create.email}, username={user_create.username}")
        
        # サンプルでデータ作成
        id_gen = random.randint(1, 1000000)
        user = User(
            id=id_gen,
            email=user_create.email,
            username=user_create.username,
            full_name=user_create.full_name,
            is_active=False,
        )
        
        logger.info(f"ユーザーを作成しました: id={id_gen}")
        return user

    @log_function(level='DEBUG')
    async def delete_user(self, userId, x_trace_id):
        # ロガー取得
        logger = get_logger()
        logger.info(f"ユーザー削除リクエスト: id={userId}")
        
        # サンプルでデータ削除
        logger.info(f"ユーザー削除完了: id={userId}")
        return None
        
    @log_function(level='DEBUG')
    async def get_user_by_id(self, userId, x_trace_id):
        # ロガー取得
        logger = get_logger()
        logger.info(f"ユーザー情報取得リクエスト: id={userId}")
        
        # サンプル実装
        if userId <= 0:
            logger.warning(f"存在しないユーザーが指定されました: id={userId}")
            raise HTTPException(status_code=404, detail="User not found")
            
        user = User(
            id=userId,
            email=f"user{userId}@example.com",
            username=f"user{userId}",
            full_name=f"User {userId}",
            is_active=True
        )
        
        logger.info(f"ユーザー情報取得完了: id={userId}")
        return user
        
    @log_function(level='DEBUG')
    async def get_users(self, x_trace_id, skip, limit):
        # ロガー取得
        logger = get_logger()
        logger.info(f"ユーザー一覧取得リクエスト: skip={skip}, limit={limit}")

        skip = int(skip)
        limit = int(limit)
        
        # サンプル実装
        users = []
        for i in range(1, min(limit+1, 10)):
            users.append(User(
                id=i,
                email=f"user{i}@example.com",
                username=f"user{i}",
                full_name=f"User {i}",
                is_active=True
            ))
            
        logger.info(f"ユーザー一覧取得完了: 件数={len(users)}")
        return users
        
    @log_function(level='DEBUG')
    async def update_user(self, userId, user_update, x_trace_id):
        # ロガー取得
        logger = get_logger()
        logger.info(f"ユーザー更新リクエスト: id={userId}")
        
        # サンプル実装
        if userId <= 0:
            logger.warning(f"存在しないユーザーが指定されました: id={userId}")
            raise HTTPException(status_code=404, detail="User not found")
            
        user = User(
            id=userId,
            email=user_update.email or f"user{userId}@example.com",
            username=user_update.username or f"user{userId}",
            full_name=user_update.full_name or f"User {userId}",
            is_active=True
        )
        
        logger.info(f"ユーザー情報更新完了: id={userId}")
        return user