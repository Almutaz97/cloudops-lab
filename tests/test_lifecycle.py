from unittest.mock import patch

from fastapi.testclient import TestClient
from app.main import app, logger


def test_application_lifecycle():
    with patch.object(logger, "info") as mock_log:
        with TestClient(app) as client:
            response = client.get("/health")
            assert response.status_code == 200

        messages = [
            call.args[0]
            for call in mock_log.call_args_list
        ]

        assert "ServiceOps application starting" in messages
        assert "ServiceOps application shutting down" in messages
