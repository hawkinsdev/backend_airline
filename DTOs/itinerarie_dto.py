from pydantic import BaseModel, Field


class SearchFlight(BaseModel):
    origin: int = Field(..., description="id del aeropuerto, consultar la lista de aeropuertos.")
    destination: int = Field(..., description="id del aeropuerto, consultar la lista de aeropuertos.")


class ScheduleResponseDto(BaseModel):
    date: str
    departure_time: str
    arrival_time: str


class SegmentResponseDto(BaseModel):
    flight_code: str
    origin: str
    destination: str
    duration: int
    frequency: str
    schedules: list[ScheduleResponseDto]


class ItineraryResponseDto(BaseModel):
    itinerary_id: int
    origin: str
    destination: str
    total_duration: int
    route: list[str]
    segments: list[SegmentResponseDto]
