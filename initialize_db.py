from config.database import Database, Base
from models.airports import Airports # noqa 401
from models.flights import Flights # noqa 401
from models.schedules import Schedules # noqa 401
from models.itineraries import Itineraries # noqa 401


def initialize_database():
    try:
        db = Database()
        Base.metadata.create_all(bind=db.engine)
        print("Database initialized successfully.")
    except Exception as e:
        print(F"Error to initialize db: {e}")


if __name__ == "__main__":
    initialize_database()
