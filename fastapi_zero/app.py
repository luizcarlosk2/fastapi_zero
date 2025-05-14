from fastapi import FastAPI
from http import HTTPStatus

from fastapi_zero.schemas import Message

app = FastAPI(title='FastAPI do Zero 2025!')


@app.get(
        '/', 
        status_code=HTTPStatus.OK, 
        response_model=Message # Força o schema de resposta
        )
def read_root():
    return {
        'message': 'Ola Mundo'
    }
