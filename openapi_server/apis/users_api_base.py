# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.create_user400_response import CreateUser400Response
from openapi_server.models.get_user_by_id404_response import GetUserById404Response
from openapi_server.models.user import User
from openapi_server.models.user_create import UserCreate
from openapi_server.models.user_update import UserUpdate


class BaseUsersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUsersApi.subclasses = BaseUsersApi.subclasses + (cls,)
    async def create_user(
        self,
        user_create: UserCreate,
        x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")],
    ) -> User:
        """新しいユーザーを作成します"""
        ...


    async def delete_user(
        self,
        userId: Annotated[StrictInt, Field(description="ユーザーID")],
        x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")],
    ) -> None:
        """特定のユーザーを削除します"""
        ...


    async def get_user_by_id(
        self,
        userId: Annotated[StrictInt, Field(description="ユーザーID")],
        x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")],
    ) -> User:
        """特定のユーザーの詳細情報を取得します"""
        ...


    async def get_users(
        self,
        x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")],
        skip: Annotated[Optional[StrictStr], Field(description="スキップするレコード数")],
        limit: Annotated[Optional[StrictStr], Field(description="取得するレコード数の上限")],
    ) -> List[User]:
        """システムに登録されているすべてのユーザーの一覧を取得します"""
        ...


    async def update_user(
        self,
        userId: Annotated[StrictInt, Field(description="ユーザーID")],
        user_update: UserUpdate,
        x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")],
    ) -> User:
        """特定のユーザーの情報を更新します"""
        ...
