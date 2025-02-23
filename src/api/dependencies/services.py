from fastapi import Depends

from core.services import CategoryService
from infrastructure.db import SQLAlchemyCategoryRepository


def get_category_service(
    repository=Depends(SQLAlchemyCategoryRepository),
) -> CategoryService:
    return CategoryService(repository)
