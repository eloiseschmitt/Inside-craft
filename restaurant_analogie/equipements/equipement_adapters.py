"""
Open/closed Responsability (O de SOLID)

On peut ajouter ElectricOven ou RobotCutter sans que ça n'impacte les chefs
"""

from typing import Iterable

from restaurant_analogie.ingredients.ingredient_dataclasses import Riz


class GasOven:
    def bake(self, item: str, minutes: int, temperature_c: int) -> None:
        print(f"[Oven] Cuisson de {item} {minutes} min à {temperature_c}°C")


class HandMixer:
    def mix(self, ingredients: Iterable[str], minutes: int) -> None:
        print(f"[Mixer] Mélange: {', '.join(ingredients)} ({minutes} min)")


class ChefKnife:
    def slice(self, item: str, thickness_mm: int) -> None:
        print(f"[Knife] Découpe de {item} en tranches de {thickness_mm} mm")


class SimpleRiceCooker:
    def cook(self, riz: Riz, water_ml: int) -> None:
        print(f"[RiceCooker] Riz {riz.grammes} g avec {water_ml} ml d'eau")
