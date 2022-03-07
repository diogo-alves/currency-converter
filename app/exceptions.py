from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class APIConnectionError(Exception):
    ...


def api_connection_exception_handler(
    request: Request,
    exc: APIConnectionError,
):
    return JSONResponse(
        status_code=status.HTTP_502_BAD_GATEWAY,
        content={'detail': 'Falha na comunicação com o servidor remoto.'},
    )


def register_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(
        APIConnectionError,
        api_connection_exception_handler,
    )
