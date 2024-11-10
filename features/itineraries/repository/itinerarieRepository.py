from helpers.repository.general_repository import SQLAlchemyRepository
from models.itineraries import Itineraries
from models.schedules import Schedules
from models.airports import Airports
from config.database import Database
from models.flights import Flights
from json import loads


class ItinerarieRepository():

    def __init__(self):
        self.db = Database()
        self.session = self.db.get_session()
        self.repository = SQLAlchemyRepository(Itineraries, self.session)

    def get_itineraries(self, origin, destination):
        try:
            itineraries = self.session.query(Itineraries).filter(
                Itineraries.origin == origin,
                Itineraries.destination == destination
            ).all()

            results = []

            for itinerary in itineraries:
                route_codes = loads(itinerary.route)

                segment_details = []
                for i in range(len(route_codes) - 1):
                    origin_code = route_codes[i]
                    destination_code = route_codes[i+1]

                    flight_segment = self.session.query(
                        Flights
                    ).join(
                        Airports, Airports.id == Flights.origin
                    ).filter(
                        Airports.code == origin_code,
                        Flights.destination_dict.has(code=destination_code)
                    ).first()

                    if flight_segment:
                        schedule = self.session.query(
                            Schedules
                        ).filter(Schedules.flight_id == flight_segment.id).all()

                        segment_info = {
                            "flight_code": flight_segment.code,
                            "origin": flight_segment.origin_dict.name,
                            "destination": flight_segment.destination_dict.name,
                            "duration": flight_segment.duration,
                            "frequency": flight_segment.frequency,
                            "schedules": [
                                {
                                    "date": s.date,
                                    "departure_time": s.departure_time,
                                    "arrival_time": s.arrival_time,
                                }
                                for s in schedule
                            ],
                        }
                        segment_details.append(segment_info)

                itinerary_info = {
                    "itinerary_id": itinerary.id,
                    "origin": itinerary.origin_dict.name,
                    "destination": itinerary.destination_dict.name,
                    "total_duration": itinerary.total_duration,
                    "route": route_codes,
                    "segments": segment_details,
                }
                results.append(itinerary_info)

            return results
        except Exception as e:
            print(f'Error to get itineraries {e}')
