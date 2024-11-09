from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from features.auth.Class.login import Login


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=401, detail="Tipo de autenticación invalida.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=401, detail="Token invalido, su sesión ha expirado.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Código de autorización invalido.")

    def verify_jwt(self, token: str) -> bool:
        isTokenValid: bool = False
        try:
            payload = Login.verify_access_token(token)
        except Exception as e:
            print("Error", e)
            payload = None

        if payload:
            isTokenValid = True
        return isTokenValid
