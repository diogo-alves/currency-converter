from fastapi import FastAPI

from . import api, exceptions

app = FastAPI(
    title="Currency Converter",
    description="Uma API REST para conversão de moedas",
    version="1.0.0",
)


@app.on_event('startup')
def startup():
    api.register_api(app)
    exceptions.register_exception_handler(app)
