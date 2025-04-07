# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.users_api_base import BaseUsersApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.create_user400_response import CreateUser400Response
from openapi_server.models.get_user_by_id404_response import GetUserById404Response
from openapi_server.models.user import User
from openapi_server.models.user_create import UserCreate
from openapi_server.models.user_update import UserUpdate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/users",
    responses={
        201: {"model": User, "description": "ユーザー作成成功"},
        400: {"model": CreateUser400Response, "description": "リクエスト形式が不正"},
    },
    tags=["users"],
    summary="新規ユーザー作成",
    response_model_by_alias=True,
)
async def create_user(
    user_create: UserCreate = Body(None, description=""),
    x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")] = Header(None, description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます"),
) -> User:
    """新しいユーザーを作成します"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().create_user(user_create, x_trace_id)


@router.delete(
    "/users/{userId}",
    responses={
        204: {"description": "削除成功"},
        404: {"model": GetUserById404Response, "description": "リソースが見つかりません"},
    },
    tags=["users"],
    summary="ユーザー削除",
    response_model_by_alias=True,
)
async def delete_user(
    userId: Annotated[StrictInt, Field(description="ユーザーID")] = Path(..., description="ユーザーID"),
    x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")] = Header(None, description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます"),
) -> None:
    """特定のユーザーを削除します"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().delete_user(userId, x_trace_id)


@router.get(
    "/users/{userId}",
    responses={
        200: {"model": User, "description": "成功"},
        404: {"model": GetUserById404Response, "description": "リソースが見つかりません"},
    },
    tags=["users"],
    summary="ユーザー情報取得",
    response_model_by_alias=True,
)
async def get_user_by_id(
    userId: Annotated[StrictInt, Field(description="ユーザーID")] = Path(..., description="ユーザーID"),
    x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")] = Header(None, description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます"),
) -> User:
    """特定のユーザーの詳細情報を取得します"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().get_user_by_id(userId, x_trace_id)


@router.get(
    "/users",
    responses={
        200: {"model": List[User], "description": "成功"},
    },
    tags=["users"],
    summary="ユーザー一覧を取得",
    response_model_by_alias=True,
)
async def get_users(
    x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")] = Header(None, description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます"),
    skip: Annotated[Optional[StrictStr], Field(description="スキップするレコード数")] = Query('0', description="スキップするレコード数", alias="skip"),
    limit: Annotated[Optional[StrictStr], Field(description="取得するレコード数の上限")] = Query('100', description="取得するレコード数の上限", alias="limit"),
) -> List[User]:
    """システムに登録されているすべてのユーザーの一覧を取得します"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().get_users(x_trace_id, skip, limit)


@router.put(
    "/users/{userId}",
    responses={
        200: {"model": User, "description": "更新成功"},
        400: {"model": CreateUser400Response, "description": "リクエスト形式が不正"},
        404: {"model": GetUserById404Response, "description": "リソースが見つかりません"},
    },
    tags=["users"],
    summary="ユーザー情報更新",
    response_model_by_alias=True,
)
async def update_user(
    userId: Annotated[StrictInt, Field(description="ユーザーID")] = Path(..., description="ユーザーID"),
    user_update: UserUpdate = Body(None, description=""),
    x_trace_id: Annotated[Optional[StrictStr], Field(description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます")] = Header(None, description="トレーサビリティID(UUID形式)。指定しない場合は自動生成されます"),
) -> User:
    """特定のユーザーの情報を更新します"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().update_user(userId, user_update, x_trace_id)
