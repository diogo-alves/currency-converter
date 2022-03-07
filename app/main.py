from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import api, exceptions
from .config import settings

app = FastAPI(
    title="Conversor de Moedas",
    description="Uma API REST para conversão de moedas com base na cotação do dólar americano (USD)",  # noqa
    version="1.0.0",
    license_info={
        'name': 'Licença de uso',
        'url': 'https://github.com/diogo-alves/currency-converter/blob/main/LICENSE',  # noqa
    },
    openapi_tags=[
        {
            'name': 'Conversão',
            'description': 'Endpoint que realiza conversões entre moedas',
        },
    ],
)

if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


@app.on_event('startup')
def startup():
    api.register_api(app)
    exceptions.register_exception_handler(app)
