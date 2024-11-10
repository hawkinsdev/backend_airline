from models.itineraries import Itineraries
from ..data.itineraries import ITINERARIES


class ItinerariesSeed:

    @classmethod
    def create_itineraries(cls, session):
        try:
            for itinerarie in ITINERARIES:
                row = Itineraries(**itinerarie)
                session.add(row)
                session.commit()

            return True
        except Exception as e:
            print(f"Error creating itineraries: {e}")
            raise e
