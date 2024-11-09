from models.airports import Airports
from ..data.airports import AIRPORTS


class AirportsSeed:

    @classmethod
    def create_airports(cls, session):
        try:
            for airport in AIRPORTS:
                exits = session.query(Airports).filter_by(code=airport['code']).first()
                if exits:
                    continue

                row = Airports(**airport)
                session.add(row)
                session.commit()

            return True
        except Exception as e:
            print(f"Error creating Airports: {e}")
            raise e
