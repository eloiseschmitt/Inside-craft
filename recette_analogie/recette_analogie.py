# P3ST0 v3rs10n by P4P4 0UR$

import threading
import warnings


def r7_pesto(u: str):
    """Traduction Python de R7_PeStO (même esprit “meme code”)."""
    toto = 80  # g of pgns ???
    cheese = "fr0maggio"  # italien ofc
    basil = "3/4 leafz?"  # idk combien ça fait
    garlic = [1, 1]  # 2 cloves, logique
    oil = f"{int(2e1)}cl maybe?"  # uhm, olive?
    tata = "bl3nd3r"  # mixeur obv

    # Step ? Mix all??? ¯\_(ツ)_/¯
    mix_result = f"{toto}+{cheese}+{basil}+{garlic}+{oil} @ {tata}"

    # setTimeout(..., 300000 / 60) -> 5000 ms (~5 s, pas 5 min)
    delay_seconds = (300000 / 60) / 1000.0

    timer = threading.Timer(delay_seconds, lambda: print("PESTO???", mix_result))
    timer.start()

    # don't forget 🍝 lol
    warnings.warn("⚠️ pasta?? achetez au shop !", stacklevel=1)

    return timer  # pour permettre au caller d'attendre la fin si besoin


# ---------------------------------------------------------------------------
# Recette : Pesto maison
# Auteur : Geoffrey Graveaud
# ---------------------------------------------------------------------------

def make_homemade_pesto() -> str:
    """
    Prépare un pesto maison pour environ 8 personnes.
    :return: Le pesto prêt à être dégusté !
    """
    ingredients = {
        "olive_oil_cl": 20,     # cl
        "garlic_cloves": 2,     # gousses
        "pine_nuts_g": 80,      # grammes
        "parmesan_g": 80,       # grammes
        "basil": "3 à 4 feuilles",
        # Variante optionnelle :
        "version_thomas": {"add_anchovies": True},
    }

    def prepare_ingredients():
        print("Découper le parmesan en tout petits morceaux.")
        print("Découper les gousses d’ail sans les écraser.")

    def blend_ingredients():
        print("Ajouter tous les ingrédients dans le mixeur.")
        print("Mixer pendant quelques minutes jusqu'à consistance homogène.")

    def season():
        print("Saler et poivrer selon vos goûts.")

    # Étapes de préparation
    prepare_ingredients()
    blend_ingredients()
    season()

    return "Votre pesto maison est prêt ! Buon Appetito 🇮🇹"


if __name__ == "__main__":
    t = r7_pesto("go")
    pesto_msg = make_homemade_pesto()
    print(pesto_msg)
    t.join()  # attendre l'affichage différé de r7_pesto
