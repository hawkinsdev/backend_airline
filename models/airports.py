from sqlalchemy import Column, Integer, DateTime, String, sql
from config.database import Base


class Airports(Base):
    __tablename__ = 'airports'

    id = Column(Integer, primary_key=True)
    code = Column(String(5), nullable=False)
    name = Column(String(45), nullable=False)
    location = Column(String(45), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=sql.func.now())
    updated_at = Column(DateTime, nullable=True)
