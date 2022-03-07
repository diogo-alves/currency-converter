import logging

from fastapi import APIRouter, FastAPI

from . import v1

log = logging.getLogger('uvicorn')


router = APIRouter()
router.include_router(v1.router)


def register_api(app: FastAPI) -> None:
    app.include_router(router)
    log.info('API registrada.')
