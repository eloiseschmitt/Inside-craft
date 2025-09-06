class RestaurantPizzaAndSushiAndIceCream:
    def __init__(self, four, spatule, pelle_a_pizza, sac_a_farine,
                 sauce_tomate, olives, feuille_de_nori,
                 saumon, avocat, riz):
        self.four = four
        self.spatule = spatule
        self.pelle_a_pizza = pelle_a_pizza
        self.sac_a_farine = sac_a_farine
        self.sauce_tomate = sauce_tomate
        self.olives = olives
        self.feuille_de_nori = feuille_de_nori
        self.saumon = saumon
        self.avocat = avocat
        self.riz = riz

    # Methods
    def prepare_sauce_tomate(self, *args, **kwargs):
        pass

    def cuire_riz(self, *args, **kwargs):
        pass

    def prepare_pate_a_pizza(self, *args, **kwargs):
        pass

    def decouper_saumon(self, *args, **kwargs):
        pass

    def decouper_avocat(self, *args, **kwargs):
        pass

    def composer_sushi(self, *args, **kwargs):
        pass

    def composer_pizza(self, *args, **kwargs):
        pass

# enfreint le Single Responsability Priciple (le S de SOLID)