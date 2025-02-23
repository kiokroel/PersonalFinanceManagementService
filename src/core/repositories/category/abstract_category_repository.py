from abc import ABC, abstractmethod

from src.core.entities import Category
from src.core.repositories.category.dto import (
    CategoryCreate,
    CategoryUpdate,
)


class AbstractCategoryRepository(ABC):
    @abstractmethod
    async def get_category(self, category_id: int) -> Category:
        pass

    @abstractmethod
    async def create_category(self, category: CategoryCreate) -> Category:
        pass

    @abstractmethod
    async def update_category(self, category: CategoryUpdate) -> Category:
        pass

    @abstractmethod
    async def delete_category(self, category_id: int) -> None:
        pass
