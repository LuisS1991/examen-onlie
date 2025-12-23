# repositories/base_repository.py
from typing import Callable, TypeVar, Generic, List, Optional, Type, Union
from sqlmodel import SQLModel, Session, select
import sqlalchemy.orm
import reflex as rx
from sqlalchemy import func

ModelType = TypeVar("ModelType", bound=SQLModel)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_session(self) -> Session:
        return rx.session()

    def get_all(self) -> List[ModelType]:
        with self.get_session() as session:
            statement = select(self.model)
            results = session.exec(statement).all()
        return results

    def get_all_with_join(
        self,
        join_loads: Optional[List[Callable]] = None,
        filters: Optional[List] = None,
    ) -> List[ModelType]:
        with self.get_session() as session:
            statement = select(self.model)

            if join_loads:
                for relation in join_loads:
                    statement = statement.options(sqlalchemy.orm.selectinload(relation))

            if filters:
                for condition in filters:
                    statement = statement.where(condition)

            results = session.exec(statement).all()
        return results

    def get_with_fillter(self, filters: Optional[List]) -> List[ModelType]:
        with self.get_session() as session:
            statement = select(self.model)
            if filters:
                for condition in filters:
                    statement = statement.where(condition)

            results = session.exec(statement).all()
        return results

    def get_by_id(self, id: int) -> Optional[ModelType]:
        with self.get_session() as session:
            return session.get(self.model, id)

    def get_by_id_with_join(
        self, id: int, join_loads: Optional[List[Callable]] = None
    ) -> Optional[ModelType]:
        with self.get_session() as session:
            statement = select(self.model).where(self.model.id == id)

            if join_loads:
                for load in join_loads:
                    statement = statement.options(sqlalchemy.orm.selectinload(load))

            result = session.exec(statement).first()
            return result

    def get_by_one_with_filters(self, filters: Optional[List]) -> Optional[ModelType]:
        with self.get_session() as session:
            statement = select(self.model)
            if filters:
                for condition in filters:
                    statement = statement.where(condition)

            result = session.exec(statement).first()
            return result

    def create(self, obj_in: Union[ModelType, dict]) -> ModelType:
        with self.get_session() as session:
            if isinstance(obj_in, dict):
                db_obj = self.model(**obj_in)
            else:
                db_obj = obj_in
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def update(self, id: int, obj_data: dict) -> Optional[ModelType]:
        with self.get_session() as session:
            obj = session.get(self.model, id)
            if not obj:
                return None
            for key, value in obj_data.items():
                setattr(obj, key, value)
            session.add(obj)
            session.commit()
            session.refresh(obj)
        return obj

    def delete(self, id: int) -> bool:
        with self.get_session() as session:
            obj = session.get(self.model, id)
            if not obj:
                return False
            session.delete(obj)
            session.commit()
        return True

    def count(self) -> int:
        with self.get_session() as session:
            statement = select(func.count()).select_from(self.model)
            result = session.exec(statement).one()
        return result
