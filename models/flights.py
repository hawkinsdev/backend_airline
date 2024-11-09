from sqlalchemy import Column, Integer, DateTime, String, sql, ForeignKey, Text
from sqlalchemy.orm import relationship
from config.database import Base


class Flights(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True)
    code = Column(String(10), nullable=False)
    origin = Column(Integer, ForeignKey('airports.id'))
    destination = Column(Integer, ForeignKey('airports.id'))
    duration = Column(Integer, nullable=False)
    frequency = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=sql.func.now())
    updated_at = Column(DateTime, nullable=True)

    origin_dict = relationship('Airports', lazy='joined', foreign_keys=[origin])
    destination_dict = relationship('Airports', lazy='joined', foreign_keys=[destination])
