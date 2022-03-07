from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import api, exceptions
from .config import settings

app = FastAPI(
    title="Currency Converter",
    description="Uma API REST para conversão de moedas",
    version="1.0.0",
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
