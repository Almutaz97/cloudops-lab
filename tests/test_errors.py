from unittest.mock import patch

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import handle_unexpected_error, logger


def test_unexpected_error_returns_safe_500():
    test_app = FastAPI()
    test_app.add_exception_handler(Exception, handle_unexpected_error)

    @test_app.get("/fail")
    def fail():
        raise RuntimeError("private-debug-detail")

    with patch.object(logger, "error") as mock_log:
        with TestClient(test_app, raise_server_exceptions=False) as client:
            response = client.get("/fail")

    assert response.status_code == 500
    assert response.json() == {"detail": "Internal server error"}
    assert "private-debug-detail" not in response.text
    mock_log.assert_called_once()
