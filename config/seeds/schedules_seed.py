from models.schedules import Schedules
from ..data.schedules import SCHEDULES


class SchedulesSeed:

    @classmethod
    def create_schedules(cls, session):
        try:
            for schedule in SCHEDULES:
                row = Schedules(**schedule)
                session.add(row)
                session.commit()

            return True
        except Exception as e:
            print(f"Error creating schedules: {e}")
            raise e
