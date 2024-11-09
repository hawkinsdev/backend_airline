from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class IRepository(Generic[T]):

    def get_by_id(self, id: int) -> T:
        raise NotImplementedError

    def get_one(self, filters: T) -> T:
        raise NotImplementedError

    def get_all(self, page: int = None, page_size: int = None) -> List[T]:
        raise NotImplementedError

    def find(self, entity: T, page: int = None, page_size: int = None, options_custom: list = []) -> Optional[T]:
        raise NotImplementedError

    def create(self, entity: T) -> T:
        raise NotImplementedError

    def update(self, id: int, entity: T) -> T:
        raise NotImplementedError

    def delete(self, id: int) -> T:
        raise NotImplementedError

    def paginate(self, query,  page: int, page_size: int) -> List[T]:
        raise NotImplementedError
