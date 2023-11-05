import pytest
from httpx import AsyncClient
from app import app
import json


class TestAPI:
    @pytest.mark.asyncio
    async def test_not_found(self):
        payload = {"build": "123"}
        async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
            not_found = await ac.post(
                "/",
                content=json.dumps(payload),
            )
        assert not_found.status_code == 404

    @pytest.mark.asyncio
    async def test_ok_response(self):
        payload = {
            "build": "forward_interest",
        }
        async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
            ok_response = await ac.post(
                "/",
                content=json.dumps(payload),
            )
        assert ok_response.status_code == 200
