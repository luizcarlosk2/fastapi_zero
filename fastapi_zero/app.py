from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='FastAPI do Zero 2025!')


@app.get(
        '/',
        status_code=HTTPStatus.OK,
        response_model=Message  # Força o schema de resposta
        )
def read_root():
    return {
        'message': 'Olá Mundo!'
    }


@app.get(
        '/ola_mundo',
         response_class=HTMLResponse,
         status_code=HTTPStatus.OK)
def ola_mundo():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Curso FastAPI Dunossauro</title>
      </head>
      <body>
        <h1>Olá Mundão!</h1>
        <p>Curso FastAPI do Zero 2025</p>
      </body>
    </html>
    """
