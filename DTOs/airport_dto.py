from pydantic import BaseModel


class AirportResponseDto(BaseModel):
    id: int
    name: str
    name_combined: str
    code: str
    location: str

    @classmethod
    def from_orm(cls, model):

        name_combined = f"{model.code} - {model.name}"
        return cls(
            id=model.id,
            name=model.name,
            name_combined=name_combined,
            code=model.code,
            location=model.location
        )

    class Config:
        from_attributes = True
