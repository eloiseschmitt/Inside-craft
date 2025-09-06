"""
Les chefs dépendent d'interfaces, pas d'implémentations directes
"""

from restaurant_analogie.equipements.equipement_ports import Oven, Mixer
from restaurant_analogie.ingredients.ingredient_dataclasses import SauceTomate, Farine


class PizzaChef:
    """Responsable de la préparation des pizzas."""
    def __init__(self, oven: Oven, mixer: Mixer):
        self.oven = oven
        self.mixer = mixer

    def prepare_sauce_tomate(self, sauce: SauceTomate) -> None:
        self.mixer.mix(
            [f"tomates {sauce.tomates_g} g", f"sel {sauce.sel_g} g", f"huile {sauce.huile_ml} ml"],
            minutes=2
        )

    def prepare_pate(self, farine: Farine, eau_ml: int, levure_g: int) -> None:
        self.mixer.mix(
            [f"farine {farine.grammes} g", f"eau {eau_ml} ml", f"levure {levure_g} g"],
            minutes=5
        )

    def cuire_pizza(self, description: str, minutes: int = 8, temperature_c: int = 260) -> None:
        self.oven.bake(description, minutes, temperature_c)
