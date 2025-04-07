# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create_user400_response import CreateUser400Response  # noqa: F401
from openapi_server.models.get_user_by_id404_response import GetUserById404Response  # noqa: F401
from openapi_server.models.user import User  # noqa: F401
from openapi_server.models.user_create import UserCreate  # noqa: F401
from openapi_server.models.user_update import UserUpdate  # noqa: F401


def test_create_user(client: TestClient):
    """Test case for create_user

    新規ユーザー作成
    """
    user_create = {"password":"strongpassword","full_name":"John Doe","email":"user@example.com","username":"johndoe"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/users",
    #    headers=headers,
    #    json=user_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_user(client: TestClient):
    """Test case for delete_user

    ユーザー削除
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/users/{userId}".format(userId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user_by_id(client: TestClient):
    """Test case for get_user_by_id

    ユーザー情報取得
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/users/{userId}".format(userId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_users(client: TestClient):
    """Test case for get_users

    ユーザー一覧を取得
    """
    params = [("skip", 0),     ("limit", 100)]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/users",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_user(client: TestClient):
    """Test case for update_user

    ユーザー情報更新
    """
    user_update = {"full_name":"John Doe","email":"user@example.com","username":"johndoe"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/users/{userId}".format(userId=56),
    #    headers=headers,
    #    json=user_update,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

