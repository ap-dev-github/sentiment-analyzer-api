import sys
from pathlib import Path

import pytest

# ../ doesnt recognize by py
sys.path.append(str(Path(__file__).resolve().parent.parent))
from app import app  # type: ignore # noqa: E402


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


# Define the test based on your endpoints
@pytest.mark.parametrize(
    "endpoint, method, input_txt, expected_status, expected_response",
    [
        (
            "/",
            "get",
            None,
            200,
            {
                "message": "Hey welcome I am running."
                "Use /analyze/text  use %20 for blank spaces."
            },
        ),
        (
            "/analyze/<input_txt>",
            "get",
            "good",
            200,
            {
                "scores":
                    {"compound": 0.4404, "neg": 0.0, "neu": 0.0, "pos": 1.0},
                "sentiment": "positive",
            },
        ),
    ],
)
def test_endpoints(
    client, endpoint, method, input_txt, expected_status, expected_response
):
    if input_txt:
        response = client.get(f"/analyze/{input_txt}")
    else:
        response = client.get(endpoint)
        assert response.status_code == expected_status, (
            f"Failed{endpoint}"
        )  # nosec
        assert response.get_json() == expected_response, (
            f"Mismatch{endpoint}"
        )  # nosec
