from features.airports.services.airport_service import AirportService
# from config.security.jwt_bearer import JWTBearer
from DTOs.airport_dto import AirportResponseDto
from fastapi import APIRouter

airport_service = AirportService()
airport_router = APIRouter(
    prefix="/airports",
    tags=["Airports"],
    # dependencies=[Depends(JWTBearer)]
)


@airport_router.get(
    path="/",
    summary="Obtiene todos los aeropuertos",
    response_model=list[AirportResponseDto]
)
async def get_airports(page: int = None, page_size: int = None):
    return airport_service.get_airports(page, page_size)
