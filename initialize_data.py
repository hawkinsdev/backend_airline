from config.database import Database
from config.seeds.airports_seed import AirportsSeed
from config.seeds.flights_seed import FlightSeed
from config.seeds.schedules_seed import SchedulesSeed
from config.seeds.itineraries_seed import ItinerariesSeed


class MainSeeds:

    @classmethod
    def main(cls):
        try:
            db = Database()
            session = db.get_session()

            AirportsSeed.create_airports(session)
            FlightSeed.create_flights(session)
            SchedulesSeed.create_schedules(session)
            ItinerariesSeed.create_itineraries(session)

            print('data initial setup successfully')
        except Exception as e:
            print(f'Error to setup data initial {e}')


if __name__ == '__main__':
    MainSeeds.main()
