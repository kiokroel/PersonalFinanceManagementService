from fastapi import APIRouter

from infrastructure.config import settings
from .finance_router import router as finance_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)


router.include_router(finance_router)
