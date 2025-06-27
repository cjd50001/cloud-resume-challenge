import pytest
import visitor_counter.__init__ as counter
from unittest.mock import MagicMock

def test_counter_get(monkeypatch):
    mock_req = MagicMock()
    mock_req.method = "GET"

    monkeypatch.setitem(counter.os.environ, "AzureWebJobsStorage", "UseDevelopmentStorage=true")

    response = counter.main(mock_req)

    assert response.status_code == 200
    assert "count" in response.get_body().decode()
