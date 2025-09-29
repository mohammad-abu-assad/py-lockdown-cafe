import datetime
from typing import Dict, Any

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: Dict[str, Any]) -> str:
        """Validate visitor and return welcome string if allowed."""
        name = visitor.get("name", "Unknown")

        vaccine = visitor.get("vaccine")
        if vaccine is None:
            raise NotVaccinatedError(name)

        expiration = vaccine.get("expiration_date")
        today = datetime.date.today()
        if expiration is None or expiration < today:
            raise OutdatedVaccineError(name, expiration)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(name)

        return f"Welcome to {self.name}"
