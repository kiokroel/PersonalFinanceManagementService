from src.core.entities import Category
from src.infrastructure.db import Category as CategoryModel


def to_entity(category: CategoryModel) -> Category:
    return Category(
        id=category.id,
        name=category.name,
        owner_id=category.owner_id,
        description=category.description,
    )
