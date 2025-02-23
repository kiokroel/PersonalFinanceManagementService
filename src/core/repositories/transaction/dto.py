from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class TransactionCreate(BaseModel):
    category_id: int
    amount: float = Field(gt=0, description="The amount must be greater than zero")
    type: TransactionType = Field(
        default=TransactionType.EXPENSE, description="The type of the transaction"
    )
    date: datetime | None = None
    description: str | None = Field(
        default=None, title="The description of the transaction", max_length=64
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "category_id": 1,
                    "amount": 99.52,
                    "type": "expense",
                    "date": "2022-01-01",
                    "description": "KFC",
                }
            ]
        }
    }


class TransactionResponse(TransactionCreate):
    id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "category_id": 1,
                    "amount": 99.52,
                    "type": "expense",
                    "date": "2022-01-01",
                    "description": "KFC",
                }
            ]
        }
    }


class TransactionUpdate(TransactionResponse):
    pass
