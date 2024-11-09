from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import and_, sql, asc, desc
from typing import List, TypeVar, Type
from .interface import IRepository
from sqlalchemy.orm import Session
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)
Model = TypeVar('Model')


class SQLAlchemyRepository(IRepository[T]):
    def __init__(self, model: Type[Model], session: Session):
        self.model = model
        self.session = session

    def refresh_db(self, model_obj: DeclarativeMeta):
        self.session.add(model_obj)
        self.session.commit()
        self.session.refresh(model_obj)
        self.session.close()

    def get_by_id(self, id: int) -> Model:
        row = self.session.query(self.model).filter(and_(self.model.id == id)).first()
        return row

    def get_one(self, filters: T) -> Model:
        """
        Consulta el último registro según los filtros proporcionados.
        Args:
            filters (T): Los filtros del modelo que se utilizarán para la consulta.
        Returns:
            Model: El último registro que coincida con los filtros.
        """
        filter_options = filters.model_dump(exclude_none=True)
        query = self.session.query(self.model)

        for field, value in filter_options.items():
            attr = getattr(self.model, field, None)
            if attr:
                query = query.filter(attr == value)

        row = query.order_by(desc(self.model.id)).first()
        return row

    def get_all(self, page: int = None, page_size: int = None, order: dict = None) -> tuple[List[Model], dict]:
        query = self.session.query(self.model)

        if order:
            field = order.get('field', None)
            direction = order.get('direction', 'asc')

            if field and hasattr(self.model, field):
                query = query.order_by(asc(getattr(self.model, field)) if direction == 'asc' else desc(getattr(self.model, field)))

        rows, pagination_info = self.paginate(query, page, page_size) if page is not None and page_size is not None else (query.all(), {})
        return rows, pagination_info

    def find(self, options: T = None, page: int = None, page_size: int = None, options_custom: list = [], order: dict = None) -> tuple[List[Model], dict]:
        filter_options = options.model_dump(exclude_none=True) if options else None
        filters = []

        if options:
            for field, value in filter_options.items():
                attr = getattr(self.model, field, None)
                if attr:
                    if isinstance(value, tuple) and field == 'created_at':
                        filters.append(attr.between(value[0], value[1]))
                    else:
                        filters.append(attr == value)

        filters.extend(options_custom)

        if not filters:
            return self.get_all(page, page_size, order)

        query = self.session.query(self.model).filter(and_(*filters))

        if order:
            field = order.get('field', None)
            direction = order.get('direction', 'asc')

            if field and hasattr(self.model, field):
                query = query.order_by(asc(getattr(self.model, field)) if direction == 'asc' else desc(getattr(self.model, field)))

        rows, pagination_info = self.paginate(query, page, page_size) if page is not None and page_size is not None else (query.all(), {})
        return rows, pagination_info

    def create(self, entity: T, exclude: dict = None) -> Model:
        row = self.model(**entity.model_dump(exclude=exclude))
        self.refresh_db(row)
        return row

    def update(self, id: int, entity: T) -> Model:
        row = self.get_by_id(id)

        if row is None:
            return None

        entity_dict = entity.model_dump(exclude_none=True)

        for field, value in entity_dict.items():
            setattr(row, field, value)

        setattr(row, 'updated_at', sql.func.now())

        self.refresh_db(row)
        return row

    def delete(self, id: int) -> None:
        row = self.get_by_id(id)

        if row is None:
            return None

        setattr(row, 'updated_at', sql.func.now())

        self.refresh_db(row)
        return row

    def paginate(self, query, page: int, page_size: int):
        total_items = query.count()
        total_pages = (total_items + page_size - 1) // page_size
        rows = query.offset((page - 1) * page_size).limit(page_size).all()

        self.session.close()
        return rows, {
            "current_page": page,
            "total_pages": total_pages,
            "page_size": page_size,
            "total_items": total_items
        }
