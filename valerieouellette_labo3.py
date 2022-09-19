class Recette:
    def __init__(self) -> None:
        self.name = ""
        self.steps = []
    
class Dejeuner:
    def __init__(self) -> None:
        self.liste_recettes = []
    
    def recette_oeuf(self):
        oeuf = Recette()
        oeuf.name = "oeuf"
        
class Diner:
    def __init__(self) -> None:
        self.liste_recettes = []

class Souper:
    def __init__(self) -> None:
        self.liste_recettes = []

class Entree:
    def __init__(self) -> None:
        self.liste_recettes = []

class Dessert:
    def __init__(self) -> None:
        self.liste_recettes = []

class Boisson:
    def __init__(self) -> None:
        self.liste_recettes = []