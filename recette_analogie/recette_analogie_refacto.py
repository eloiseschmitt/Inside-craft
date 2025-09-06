# Recette : Pesto maison
# Auteur : Geoffrey Graveaud

def make_homemade_pesto() -> str:
    """
    Prépare un pesto maison pour environ 8 personnes.
    :return: Le pesto prêt à être dégusté !
    """
    ingredients = {
        "olive_oil_cl": 20,          # cl
        "garlic_cloves": 2,          # gousses
        "pine_nuts_g": 80,           # grammes
        "parmesan_g": 80,            # grammes
        "basil": "3 à 4 feuilles",
        # Variante optionnelle :
        "version_thomas": {"add_anchovies": True},
    }

    # Étapes internes (fonctions imbriquées comme en JS)
    def prepare_ingredients():
        print("Découper le parmesan en tout petits morceaux.")
        print("Découper les gousses d’ail sans les écraser.")

    def blend_ingredients():
        print("Ajouter tous les ingrédients dans le mixeur.")
        print("Mixer pendant quelques minutes jusqu'à consistance homogène.")

    def season():
        print("Saler et poivrer selon vos goûts.")

    # Exécution des étapes
    prepare_ingredients()
    blend_ingredients()
    season()

    return "Votre pesto maison est prêt ! Buon Appetito 🇮🇹"


# Exécution
if __name__ == "__main__":
    pesto = make_homemade_pesto()
    print(pesto)
