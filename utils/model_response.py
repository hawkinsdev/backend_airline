from sqlalchemy.orm import class_mapper
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime, date


# Clase encargada de armar el response para las apis
class ModelResponse():
    # Método de respuesta
    @classmethod
    def aws(cls, data: dict):

        data['data'] = data.get('data', [])
        data['error'] = data.get('error', False)

        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        }
        return JSONResponse(
            status_code=data['statusCode'],
            headers=headers,
            content=jsonable_encoder(data)
        )

    @classmethod
    def get_body(cls, status_code: int = 200, error: bool = False, data=[], message: str = "Petición exitosa."):
        data = {
            'statusCode': status_code,
            'error': error,
            'data': data,
            'message': message,
        }
        return cls.aws(data)

    # Método de respuesta
    @classmethod
    def error(cls,  message: str = 'Error del cliente'):
        return cls.get_body(400, message=message)

    @classmethod
    def validation_error(cls, errs=[]):
        # Captura la excepción de validación y devuelve un mensaje de error al cliente
        error_messages = []
        for error in errs.errors():
            if isinstance(error["loc"], tuple):
                field = ".".join(str(loc) for loc in error["loc"])
            else:
                field = error["loc"]
            error_msg = error["msg"]
            error_messages.append(f"{field}: {error_msg}")

        return cls.unprocessable_entity(data=error_messages)

    # Método de respuesta
    @classmethod
    def success(cls, data: list = [], message: str = 'Petición exitosa.'):
        return cls.get_body(data=data, message=message)

    # Creación exitosa
    @classmethod
    def success_create(cls, data: list = [], message: str = 'El registro ha sido exitoso.'):
        return cls.get_body(201, data=data, message=message)

    # Método de respuesta
    @classmethod
    def bad_request(cls, message: str = 'Error en la petición.', data=[]):
        return cls.get_body(400, True, data=data, message=message)

    # Método de respuesta
    @classmethod
    def not_found(cls, message: str = 'Recurso no encontrado.'):
        return cls.get_body(404, True, message=message)

    # Método de respuesta
    @classmethod
    def unauthorized(cls):
        return cls.get_body(401, True, message='No autorizado.')

    # Método de respuesta
    @classmethod
    def forbidden(cls):
        return cls.get_body(403, True, message='forbidden.')

    # Método de respuesta
    @classmethod
    def method_not_allowed(cls):
        return cls.get_body(405, True, message='Método no permitido.')

    # Método de respuesta
    @classmethod
    def not_acceptable(cls):
        return cls.get_body(406, True, message='Not acceptable.')

    # Método de respuesta
    @classmethod
    def conflict(cls):
        return cls.get_body(409, True, message='Conflict.')

    # Método de respuesta
    @classmethod
    def unsupported_media_type(cls):
        return cls.get_body(415, True, message='Unsupported Media Type')

    # Método de respuesta
    @classmethod
    def too_many_requests(cls):
        return cls.get_body(429, True, message='Demasiadas solicitudes')

    # Método de respuesta
    @classmethod
    def unprocessable_entity(cls, data=[]):
        return cls.get_body(422, True, data, 'Payload incorrecto')

    # Método de respuesta
    @classmethod
    def internal_server_error(cls):
        return cls.get_body(500, True, message='Error interno del servidor')

    # Método de respuesta
    @classmethod
    def service_unavailable(cls):
        return cls.get_body(503, True, message='Servicio no disponible')

    # Método de respuesta
    @classmethod
    def gateway_timeout(cls):
        return cls.get_body(504, True, message='Tiempo de espera agotado')

    @classmethod
    def to_dict(cls, obj, with_relationships=False):
        data = {}
        mapper = class_mapper(obj.__class__)

        for column in mapper.columns:
            value = getattr(obj, column.key)
            if isinstance(value, datetime) or isinstance(value, date):
                data[column.key] = str(value)
            else:
                data[column.key] = value

        if with_relationships:
            for relationship in mapper.relationships:
                related_obj = getattr(obj, relationship.key)

                if related_obj is not None:
                    if relationship.uselist:
                        data[relationship.key] = [cls.to_dict(item, with_relationships=True) for item in related_obj]
                    else:
                        data[relationship.key] = cls.to_dict(related_obj, with_relationships=True)

        return data
