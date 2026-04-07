from typing import Any, List, Optional
from pydantic import BaseModel


class OriginPlanet(BaseModel):
    id: int
    name: str
    isDestroyed: bool
    description: str
    image: str
    deletedAt: Any | None


class Transformation(BaseModel):
    id: int
    name: str
    image: str
    ki: str
    deletedAt: Any | None


class Character(BaseModel):
    id: int
    name: str
    ki: str
    maxKi: str
    race: str
    gender: str
    description: str
    image: str
    affiliation: str
    deletedAt: Any | None
    originPlanet: OriginPlanet | None = None
    transformations: List[Transformation] | None = None
