from restaurant_analogie.equipements.equipement_ports import Cutter, RiceCooker
from restaurant_analogie.ingredients.ingredient_dataclasses import Riz, Poisson, Legume, FeuilleNori


class SushiChef:
    """Responsable des sushis."""
    def __init__(self, cutter: Cutter, rice_cooker: RiceCooker):
        self.cutter = cutter
        self.rice_cooker = rice_cooker

    def cuire_riz(self, riz: Riz, water_ml: int) -> None:
        self.rice_cooker.cook(riz, water_ml)

    def decouper_poisson(self, poisson: Poisson, thickness_mm: int = 3) -> None:
        self.cutter.slice(f"{poisson.espece} {poisson.grammes} g", thickness_mm)

    def decouper_legume(self, legume: Legume, thickness_mm: int = 3) -> None:
        self.cutter.slice(f"{legume.nom} {legume.grammes} g", thickness_mm)

    def composer_sushi(self, nori: FeuilleNori) -> None:
        print(f"[Sushi] Assemblage avec {nori.feuilles} feuille(s) de nori")
