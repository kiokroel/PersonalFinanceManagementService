from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=32)
    description: str | None = Field(
        default=None, title="The description of the category", max_length=128
    )
    owner_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "Markets",
                    "owner_id": 1,
                }
            ]
        }
    }


class CategoryResponse(CategoryCreate):
    id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Foo",
                    "description": "Markets",
                    "owner_id": 1,
                }
            ]
        }
    }


class CategoryUpdate(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=32)
    description: str | None = Field(
        default=None, title="The description of the category", max_length=128
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Foo",
                    "description": "Markets",
                }
            ]
        }
    }
