from fastapi import APIRouter

from datetime import datetime

from fastapi.params import Depends

from api.dependencies.services import get_category_service
from core.services import CategoryService
from infrastructure.config import settings

from core.repositories.category.dto import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)
from core.repositories.transaction.dto import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse,
    TransactionType,
)

router = APIRouter(prefix=settings.api.v1.finance, tags=["Finance"])


@router.get("/get_category/{id}", response_model=CategoryResponse | None)
async def get_category(
    id: int, category_service: CategoryService = Depends(get_category_service)
):
    category = await category_service.get_category(id)
    return category


@router.post("/create_category", response_model=CategoryResponse)
async def create_category(
    category: CategoryCreate,
    category_service: CategoryService = Depends(get_category_service),
):
    result = await category_service.create_category(category)
    return result


@router.put("/update_category/{id}", response_model=CategoryResponse)
async def update_category(
    category: CategoryUpdate,
    category_service: CategoryService = Depends(get_category_service),
):
    result = await category_service.update_category(category)
    return result


@router.delete("/delete_category/{id}")
async def delete_category(
    id: int, category_service: CategoryService = Depends(get_category_service)
):
    await category_service.delete_category(id)
    return {"id": id}


@router.get("/get_transaction/{id}", response_model=TransactionResponse)
async def get_transaction(id: int):
    return TransactionResponse(
        id=id,
        category_id=1,
        amount=1,
        type=TransactionType.EXPENSE,
        date=datetime.now(),
        description="test",
    )


@router.post("/create_transaction", response_model=TransactionResponse)
async def create_transaction(transaction: TransactionCreate):
    return TransactionResponse(id=1, **transaction.model_dump())


@router.put("/update_transaction/{id}", response_model=TransactionResponse)
async def update_transaction(transaction: TransactionUpdate):
    return TransactionResponse(**transaction.model_dump())


@router.delete("/delete_transaction/{id}")
async def delete_transaction(id: int):
    return {"id": id}
