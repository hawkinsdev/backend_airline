from ..repository.airport_repository import AirportRepository
from utils.model_response import ModelResponse
from DTOs.airport_dto import AirportResponseDto


class AirportService(ModelResponse, AirportRepository):

    def get_airports(self, page: int = None, page_size: int = None):
        try:
            _rows, pagination_items = self.repository.get_all(page, page_size)

            response = {
                "data": [AirportResponseDto.from_orm(client) for client in _rows],
                "pagination_items": pagination_items
            }
            return self.success(response)
        except ValueError as e:
            print(f'error to get airports {e}')
            raise e
        except Exception as e:
            print(f'error to get airports {e}')
            raise e
