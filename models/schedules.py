from sqlalchemy import Column, Integer, DateTime, sql, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from config.database import Base


class Schedules(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    date = Column(Date, nullable=False)
    departure_time = Column(Time, nullable=False)
    arrival_time = Column(Time, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=sql.func.now())
    updated_at = Column(DateTime, nullable=True)

    flight_dict = relationship('Flights', lazy='joined')
