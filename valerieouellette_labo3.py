class Etape:
    def __init__(self, desc, tmps) -> None:
        self.description = desc
        self.temps = tmps
    
    def __str__(self) -> str:
        return (f"{self.description}({self.temps}min)")

class Recette:
    def __init__(self, nom, liste_etapes) -> None:
        self.nom = nom
        self.etapes = liste_etapes

    def __str__(self) -> str:
        recette_string = self.nom
        for etape in self.etapes:
            recette_string += str(etape) + "\n"
        return recette_string

class Restaurant:

    HEURES_DEJEUNER = 6, 12
    HEURES_DINER = 11, 15
    HEURES_SOUPER = 15, 21
    HEURES_ENTREE = 6, 21
    HEURES_DESSERT = 11, 21
    HEURES_BOISSON = 6, 21

    def __init__(self) -> None:
        self.recettes_dejeuner = []
        self.recettes_diner = []
        self.recettes_souper = []
        self.recettes_entree = []
        self.recettes_dessert = []
        self.recettes_boisson = []
    
