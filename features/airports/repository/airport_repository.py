from config.database import Database
from models.airports import Airports
from helpers.repository.general_repository import SQLAlchemyRepository


class AirportRepository():

    def __init__(self):
        self.db = Database()
        self.session = self.db.get_session()
        self.repository = SQLAlchemyRepository(Airports, self.session)
