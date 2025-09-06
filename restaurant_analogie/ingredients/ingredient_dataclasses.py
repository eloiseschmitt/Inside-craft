from dataclasses import dataclass


@dataclass(frozen=True)
class SauceTomate:
    tomates_g: int
    sel_g: int = 5
    huile_ml: int = 10


@dataclass(frozen=True)
class Farine:
    grammes: int


@dataclass(frozen=True)
class Riz:
    grammes: int


@dataclass(frozen=True)
class Poisson:
    espece: str
    grammes: int


@dataclass(frozen=True)
class Legume:
    nom: str
    grammes: int


@dataclass(frozen=True)
class FeuilleNori:
    feuilles: int
