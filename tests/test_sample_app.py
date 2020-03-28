import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_list_dogs(client):
    response = client.get("/dogs")
    response_data = response.get_json()
    assert response.status_code == 200
    assert response_data == [
        {"dog_id": 1, "name": "Matthew"},
        {"dog_id": 2, "name": "Mona"},
    ]


def test_greet_matthew(client):
    response = client.post("/dogs/1", json={"greet": "Hello!"})
    response_data = response.get_json()
    assert response.status_code == 200
    assert response_data == {"Matthew": "Yelp!"}


def test_greet_mona(client):
    response = client.post("/dogs/2", json={"greet": "Hello!"})
    response_data = response.get_json()
    assert response.status_code == 200
    assert response_data == {"Mona": "Yelp!"}


def test_not_json(client):
    response = client.post("/dogs/1")
    response_data = response.get_json()
    assert response.status_code == 400
    assert response_data == {
        "error": 'Post JSON like {"greet": "Hello!"} with application/json.'
    }


def test_no_greet(client):
    response = client.post("/dogs/1", json={"greeet": "Hello!"})
    response_data = response.get_json()
    assert response.status_code == 400
    assert response_data == {"error": "JSON must have 'greet' key."}


def test_static_response(client):
    response = client.get("/")
    assert response.status_code == 301
    assert response.headers["location"] == "http://localhost/dogs"


def test_iterable(client):
    response = client.get("/iterable")
    response_data = response.get_data(as_text=True)
    assert response.status_code == 200
    assert response_data == "12345"


def test_not_found(client):
    response = client.post("/dogs/3", json={"greet": "Hello!"})
    response_data = response.get_json()
    assert response.status_code == 404
    assert response_data == {"error": "Not Found"}


def test_method_not_allowed(client):
    response = client.get("/dogs/1")
    response_data = response.get_json()
    assert response.status_code == 405
    assert response_data == {"error": "Method Not Allowed"}


def test_internal_server_error(client):
    response = client.get("/misconfiguration")
    response_data = response.get_json()
    assert response.status_code == 500
    assert response_data == {"error": "Internal Server Error"}
