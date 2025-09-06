from restaurant_analogie.ingredients.ingredient_dataclasses import SauceTomate, Farine, Riz, Poisson, Legume, \
    FeuilleNori
from restaurant_analogie.pizza_chef import PizzaChef
from restaurant_analogie.sushi_chef import SushiChef


class Restaurant:
    """Coordonne les ateliers (pizza, sushi) sans connaître les détails bas niveau."""
    def __init__(self, pizza_chef: PizzaChef, sushi_chef: SushiChef):
        self.pizza_chef = pizza_chef
        self.sushi_chef = sushi_chef

    # Cas d’usage “pizza”
    def composer_pizza_margherita(self) -> None:
        self.pizza_chef.prepare_sauce_tomate(SauceTomate(tomates_g=400))
        self.pizza_chef.prepare_pate(Farine(grammes=250), eau_ml=150, levure_g=5)
        self.pizza_chef.cuire_pizza("Pizza Margherita")

    # Cas d’usage “sushi”
    def composer_sushi_saumon_avocat(self) -> None:
        self.sushi_chef.cuire_riz(Riz(grammes=180), water_ml=200)
        self.sushi_chef.decouper_poisson(Poisson("saumon", 120))
        self.sushi_chef.decouper_legume(Legume("avocat", 80))
        self.sushi_chef.composer_sushi(FeuilleNori(feuilles=2))
