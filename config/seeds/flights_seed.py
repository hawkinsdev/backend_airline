from models.flights import Flights
from ..data.flights import FLIGHTS


class FlightSeed:

    @classmethod
    def create_flights(cls, session):
        try:
            for flight in FLIGHTS:
                exits = session.query(Flights).filter_by(code=flight['code']).first()
                if exits:
                    continue

                row = Flights(**flight)
                session.add(row)
                session.commit()

            return True
        except Exception as e:
            print(f"Error creating flights: {e}")
            raise e
