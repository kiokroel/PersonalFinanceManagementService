from sqlalchemy import Integer, Column, Float, String, Enum, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from core.entities import TransactionType
from .base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(
        Integer, ForeignKey("categories.id"), nullable=False, index=True
    )
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    date = Column(Integer, nullable=True)
    description = Column(String(128), nullable=True)

    category = relationship("Category", back_populates="transactions")

    __table_args__ = (CheckConstraint("amount >= 0", name="check_amount_positive"),)
