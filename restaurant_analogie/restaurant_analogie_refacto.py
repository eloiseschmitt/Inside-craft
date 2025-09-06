"""
Responsabilités claires
Injections de dépendance

On va séparer les métiers, les équipements, les ingrédients et créer un chef d'orchestre (autrement appelé façade)
"""
from restaurant_analogie.equipements.equipement_adapters import GasOven, HandMixer, ChefKnife, SimpleRiceCooker
from restaurant_analogie.pizza_chef import PizzaChef
from restaurant_analogie.restaurant_facade import Restaurant
from restaurant_analogie.sushi_chef import SushiChef


def build_restaurant() -> Restaurant:
    oven = GasOven()
    mixer = HandMixer()
    knife = ChefKnife()
    rice_cooker = SimpleRiceCooker()

    pizza_chef = PizzaChef(oven=oven, mixer=mixer)
    sushi_chef = SushiChef(cutter=knife, rice_cooker=rice_cooker)

    return Restaurant(pizza_chef=pizza_chef, sushi_chef=sushi_chef)


if __name__ == "__main__":
    resto = build_restaurant()
    resto.composer_pizza_margherita()
    resto.composer_sushi_saumon_avocat()
