from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_ola_mundo():
    client = TestClient(app)

    response = client.get('/ola_mundo')

    assert response.status_code == HTTPStatus.OK
    assert "<h1>Olá Mundão!</h1>" in response.text
    assert "Curso FastAPI do Zero 2025" in response.text
    assert response.headers["content-type"].startswith("text/html")
