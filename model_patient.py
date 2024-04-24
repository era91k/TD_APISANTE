from pydantic import BaseModel, validator
from ssn_validator import SSNValidator

class Patient(BaseModel):
    nom: str
    prenom: str
    ssn: int

    @validator('ssn')
    def validate_ssn(cls, value):
        return SSNValidator.validate_ssn(value)


