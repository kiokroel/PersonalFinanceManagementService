from abc import ABC, abstractmethod

from core.repositories.transaction.dto import TransactionUpdate
from src.core.entities import Transaction
from src.core.repositories.transaction.dto import TransactionCreate


class AbstractTransactionRepository(ABC):
    @abstractmethod
    async def create_transaction(
        self, create_transaction: TransactionCreate
    ) -> Transaction:
        pass

    @abstractmethod
    async def get_transactions(self, category_id: int) -> list[Transaction]:
        pass

    @abstractmethod
    async def delete_transaction(self, transaction_id: int) -> None:
        pass

    @abstractmethod
    async def update_transaction(self, transaction: TransactionUpdate) -> Transaction:
        pass
