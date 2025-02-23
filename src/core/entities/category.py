from dataclasses import dataclass


@dataclass
class Category:
    id: int
    name: str
    owner_id: int
    description: str | None = None
