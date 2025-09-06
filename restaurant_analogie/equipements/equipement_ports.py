from typing import Protocol, Iterable

from restaurant_analogie.ingredients.ingredient_dataclasses import Riz


class Oven(Protocol):
    def bake(self, item: str, minutes: int, temperature_c: int) -> None: ...


class Mixer(Protocol):
    def mix(self, ingredients: Iterable[str], minutes: int) -> None: ...


class Cutter(Protocol):
    def slice(self, item: str, thickness_mm: int) -> None: ...


class RiceCooker(Protocol):
    def cook(self, riz: Riz, water_ml: int) -> None: ...
