from fastapi import Depends
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from core.entities import Category
from core.repositories import AbstractCategoryRepository
from core.repositories.category.dto import CategoryCreate, CategoryUpdate
from infrastructure.db.db_helper import db_helper
from infrastructure.db.mappers.category_mapper import to_entity
from infrastructure.db import Category as CategoryModel


class SQLAlchemyCategoryRepository(AbstractCategoryRepository):
    def __init__(self):
        pass

    @db_helper.connection
    async def create_category(
        self,
        category: CategoryCreate,
        session: AsyncSession = None,
    ) -> Category:
        category_model = CategoryModel(**category.model_dump())
        session.add(category_model)
        await session.commit()
        await session.refresh(category_model)
        return to_entity(category_model)

    @db_helper.connection
    async def get_category(
        self,
        category_id: int,
        session: AsyncSession = None,
    ) -> Category | None:
        stmt = select(CategoryModel).where(CategoryModel.id == category_id)
        result = await session.execute(stmt)
        category_model: CategoryModel | None = result.one_or_none()
        if category_model is None:
            return None
        return to_entity(category_model)

    @db_helper.connection
    async def delete_category(
        self,
        category_id: int,
        session: AsyncSession = None,
    ) -> None:
        stmt = delete(CategoryModel).where(CategoryModel.id == category_id)
        await session.execute(stmt)
        await session.commit()

    @db_helper.connection
    async def update_category(
        self,
        category: CategoryUpdate,
        session: AsyncSession = None,
    ) -> Category | None:
        stmt = (
            update(CategoryModel)
            .where(CategoryModel.id == category.id)
            .values(**category.model_dump(exclude_unset=True))
        )
        await session.execute(stmt)
        update_category: CategoryModel | None = await session.get(
            CategoryModel, category.id
        )
        await session.commit()
        if update_category is None:
            return None
        return to_entity(update_category)
