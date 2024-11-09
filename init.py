from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers.list_routers import ROUTERS
from fastapi.exceptions import RequestValidationError
from utils.model_response import ModelResponse
from helpers.exception import UserException

app = FastAPI(
    title="AIRPLANE",
    description="Punto de Pago Air (PPA), una aerolínea en fase de lanzamiento planea iniciar \
        operaciones en 8 aeropuertos nacionales colombianos: BOG, MDE, BAQ, BGA, SMR, CTG, CLO y EOH. \
        La aerolínea ha establecido un itinerario semanal fijo, es decir, los mismos vuelos operarán los \
        mismos días cada semana. Sin embargo, debido al tamaño inicial de la flota, no todos los aeropuertos \
        estarán conectados por vuelos directos.",
    version="1.0.0",
)

origins = ['*']

for router in ROUTERS:
    app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return ModelResponse.validation_error(exc)


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return ModelResponse.internal_server_error()


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return ModelResponse.internal_server_error()


@app.exception_handler(UserException)
async def user_exception_handler(request: Request, exc: UserException):
    print(exc)
    if exc.status_code == 400:
        return ModelResponse.bad_request(data=exc.data, message=exc.message)
    if exc.status_code == 401:
        return ModelResponse.unauthorized()
    if exc.status_code == 403:
        return ModelResponse.forbidden()
    if exc.status_code == 422:
        return ModelResponse.unprocessable_entity(data=exc.data)


@app.get("/", tags=["Welcome"])
def welcome():
    return {"message": "welcome to backend airplane, Copyright © 2024 Jesus Varela."}
