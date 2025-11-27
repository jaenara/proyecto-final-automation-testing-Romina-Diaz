import requests

def test_api_delete_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)

    assert response.status_code in (200, 204)
