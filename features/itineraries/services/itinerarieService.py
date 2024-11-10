from ..repository.itinerarieRepository import ItinerarieRepository
from utils.model_response import ModelResponse
from DTOs.itinerarie_dto import SearchFlight


class ItinerarieService(ModelResponse, ItinerarieRepository):

    def search_itineraries(self, filter: SearchFlight):
        try:
            itineraries = self.get_itineraries(filter.origin, filter.destination)
            return self.success(itineraries)
        except ValueError as e:
            print(f'value error to search_itineraries {e}')
            raise e
        except Exception as e:
            print(f'error to search_itineraries {e}')
            raise e
