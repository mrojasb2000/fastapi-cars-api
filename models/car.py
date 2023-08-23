from typing import List
from enum import Enum
from pydantic import BaseModel, ValidationError


class Fuel(str, Enum):
    PETROL = 'PETROL'
    DIESEL = 'DIESEL'
    LPG = 'LPG'


class Car(BaseModel):
    brand: str
    make: str
    year: int
    fuel: Fuel
    countries: List[str]
    note: str = "No note"
