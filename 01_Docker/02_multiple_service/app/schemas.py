from typing import List, Union
from pydantic import BaseModel


class CarCreate(BaseModel):
    name: str
    number: str




