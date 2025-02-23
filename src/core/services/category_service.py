from core.entities import Category
from src.core.repositories import AbstractCategoryRepository


class CategoryService:
    def __init__(self, category_repository: AbstractCategoryRepository):
        self.category_repository = category_repository

    async def create_category(self, category) -> Category:
        return await self.category_repository.create_category(category)

    async def update_category(self, category) -> Category | None:
        return await self.category_repository.update_category(category)

    async def get_category(self, category_id: int) -> Category | None:
        return await self.category_repository.get_category(category_id)

    async def delete_category(self, category_id: int):
        return await self.category_repository.delete_category(category_id)
