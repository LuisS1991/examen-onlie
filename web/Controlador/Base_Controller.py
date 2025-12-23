# controllers/base_controller.py
from typing import Callable, Generic, TypeVar, Type, List, Optional, Union
from sqlmodel import SQLModel, Session
from web.Repositorio.Base_Repositorio import BaseRepository
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseController(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.repo = BaseRepository(model)
        self.model = model

    def get_session(self) -> Session:
        return self.repo.get_session()

    async def get_all(self) -> List[ModelType]:
        return self.repo.get_all()

    async def get_all_with_join(
        self,
        join_loads_params: Optional[List[Callable]] = None,
        filters_params: Optional[List] = None,
    ) -> List[ModelType]:
        return self.repo.get_all_with_join(
            join_loads=join_loads_params, filters=filters_params
        )

    async def get_by_id(self, id: int) -> Optional[ModelType]:
        return self.repo.get_by_id(id)

    async def get_by_one_with_filters(
        self, filters: Optional[List]
    ) -> Optional[ModelType]:
        return self.repo.get_by_one_with_filters(filters=filters)

    async def get_by_id_with_join(
        self, id_params: int, join_loads_params: Optional[List[Callable]] = None
    ) -> ModelType:
        return self.repo.get_by_id_with_join(id=id_params, join_loads=join_loads_params)

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        obj_data = obj_in.model_dump()
        return self.repo.create(obj_data)

    async def update(self, id: int, obj_in: UpdateSchemaType) -> ModelType:
        return self.repo.update(id, obj_in.model_dump())

    async def delete(self, id: int) -> bool:
        return self.repo.delete(id)

    async def get_with_fillter(self, filters_param: Optional[List]) -> List[ModelType]:
        return self.repo.get_with_fillter(filters=filters_param)

    async def count(self) -> int:
        return self.repo.count()
