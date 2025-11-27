import requests

def test_api_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Jae Test",
        "body": "Contenido de prueba",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Jae Test"
    assert data["body"] == "Contenido de prueba"
    assert data["userId"] == 1
