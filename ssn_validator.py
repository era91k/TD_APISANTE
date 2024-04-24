
from pydantic import BaseModel, ValidationError

class SSNValidator:
    @classmethod
    def validate_ssn(cls, value):
        ssn = str(value)
        if len(ssn) != 13:
            raise ValueError("Le numéro de sécurité sociale doit contenir exactement 13 chiffres")

        gender_digit = int(ssn[0])
        if gender_digit not in [1, 2]:
            raise ValueError("Le premier chiffre doit être 1 pour un homme ou 2 pour une femme")

        birth_year = int(ssn[1:3])
        if birth_year < 0 or birth_year > 99:
            raise ValueError("Année de naissance invalide")

        birth_month = int(ssn[3:5])
        if birth_month < 1 or birth_month > 12:
            raise ValueError("Mois de naissance invalide")

        department = int(ssn[5:7])
        if department < 1 or department > 99:
            raise ValueError("Département de naissance invalide")

        country_id = int(ssn[7:10])
        if country_id < 1 or country_id > 999:
            raise ValueError("Identifiant du pays de naissance invalide")

        birth_index = int(ssn[10:13])
        if birth_index < 1 or birth_index > 999:
            raise ValueError("Indice de naissance invalide")

        return value
