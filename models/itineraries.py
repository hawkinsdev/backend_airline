from sqlalchemy import Column, Integer, DateTime, sql, ForeignKey, Text
from sqlalchemy.orm import relationship
from config.database import Base


class Itineraries(Base):
    __tablename__ = 'itineraries'

    id = Column(Integer, primary_key=True)
    origin = Column(Integer, ForeignKey('airports.id'))
    destination = Column(Integer, ForeignKey('airports.id'))
    route = Column(Text, nullable=False)
    total_duration = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=sql.func.now())
    updated_at = Column(DateTime, nullable=True)

    origin_dict = relationship('Airports', lazy='joined', foreign_keys=[origin])
    destination_dict = relationship('Airports', lazy='joined', foreign_keys=[destination])
