from features.itineraries.services.itinerarieService import ItinerarieService
# from config.security.jwt_bearer import JWTBearer
from DTOs.itinerarie_dto import ItineraryResponseDto, SearchFlight
from fastapi import APIRouter

itinerarie_service = ItinerarieService()
itinerarie_router = APIRouter(
    prefix="/itineraries",
    tags=["Itineraries"],
    # dependencies=[Depends(JWTBearer)]
)


@itinerarie_router.post(
    path="/",
    summary="Obtiene todos los vuelos directos o escala",
    response_model=list[ItineraryResponseDto]
)
async def get_airports(filter: SearchFlight):
    return itinerarie_service.search_itineraries(filter)
