from sqlalchemy import Integer, Column, String, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), nullable=False)
    description = Column(String(128), nullable=True)
    owner_id = Column(Integer, nullable=False, index=True)

    transactions = relationship("Transaction", back_populates="category")

    __table_args__ = (
        UniqueConstraint("name", "owner_id", name="unique_category_name_per_owner"),
    )
