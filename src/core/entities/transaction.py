from enum import Enum
from datetime import datetime
from dataclasses import dataclass


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class Transaction:
    id: int
    category_id: int
    amount: float
    type: TransactionType
    date: datetime | None = None
    description: str | None = None
