from src.core.repositories import AbstractTransactionRepository


class TransactionService:
    def __init__(self, transaction_repository: AbstractTransactionRepository):
        self.transaction_repository = transaction_repository

    def create_transaction(self, transaction):
        pass

    def get_transactions(self, transaction_id: int):
        pass

    def delete_transaction(self, transaction_id: int):
        pass

    def update_transaction(self, transaction):
        pass
