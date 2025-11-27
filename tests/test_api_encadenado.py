import requests

def test_api_encadenado_crear_y_listar():
    # 1) Crear un recurso (POST)
    url_post = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Encadenado Test",
        "body": "Este post fue creado para el test encadenado.",
        "userId": 99
    }

    response_post = requests.post(url_post, json=payload)

    # Validar creación
    assert response_post.status_code == 201
    data_post = response_post.json()
    created_id = data_post.get("id")
    assert created_id is not None  # se generó un ID

    # 2) "Encadenar" con un GET válido
    # En JSONPlaceholder, los posts creados NO persisten,
    # así que verificamos que el servicio responda bien para GET general.
    url_list = "https://jsonplaceholder.typicode.com/posts"
    response_list = requests.get(url_list)

    assert response_list.status_code == 200
    posts = response_list.json()

    # Validar estructura mínima
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert "title" in posts[0]
    assert "body" in posts[0]
