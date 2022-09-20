class Repas:
    def __init__(self) -> None:
        self.liste_recettes = []
        self.duree_preparation = 0
        self.recette()
    
    def recette(self):
        pass
    
class Dejeuner(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.heure_debut = 6
        self.heure_fin = 12

class Diner(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.heure_debut = 11
        self.heure_fin = 15

class Souper(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.heure_debut = 15
        self.heure_fin = 21

class Dessert(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.heure_debut = 11
        self.heure_fin = 21

class Boisson(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.heure_debut = 6
        self.heure_fin = 21

class Entree(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.heure_debut = 6
        self.heure_fin = 21

class Oeufs(Dejeuner):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Faire cuire les oeufs", 4)
        etapes[2] = ("Réchauffer les pommes de terre", 2)
        etapes[3] = ("Couper les fruits", 2)
        self.liste_recettes.append(etapes)

class PainDore(Dejeuner):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Tremper le pain dans le mélange", 1)
        etapes[2] = ("Faire cuire dans la poèle", 4)
        etapes[3] = ("Couper les fruits", 2)
        Repas().liste_recettes.append(etapes)
        
class Crepes(Dejeuner):
    def __init__(self) -> None:
        self.__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Battre le mélange", 1)
        etapes[2] = ("Faire cuire dans la poèle", 5)
        etapes[3] = ("Couper les fruits", 2)
        self.liste_recettes.append(etapes)

class CroquettePoulet(Diner):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Mettre les morceaux de poulet dans la chapelure", 2)
        etapes[2] = ("Faire frire le poulet", 5)
        etapes[3] = ("Réchauffer les pommes de terres", 2)
        self.liste_recettes.append(etapes)

class SandwichThon(Diner):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Mettre le pain au four", 3)
        etapes[2] = ("Tartiner le pain", 1)
        etapes[3] = ("Servir la salade", 1)
        self.liste_recettes.append(etapes)

class Macaronis(Diner):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Faire bouillir l'eau", 3)
        etapes[2] = ("Faire cuire les macaronis", 7)
        etapes[3] = ("Réchauffer la sauce", 2)
        self.liste_recettes.append(etapes)

class Saumon(Souper):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Faire chauffer l'huile dans la poèle", 1)
        etapes[2] = ("Faire cuire le saumon", 5)
        etapes[3] = ("Réchauffer le riz", 2)
        self.liste_recettes.append(etapes)

class PitaFalafel(Souper):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Faire frire les falafels", 5)
        etapes[2] = ("Réchauffer le pain pita", 2)
        etapes[3] = ("Garnir le pain avec les falafels", 2)
        self.liste_recettes.append(etapes)

class PizzaVege(Souper):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Préparer la pâte", 3)
        etapes[2] = ("Garnir la pizza", 2)
        etapes[3] = ("Cuire la pizza", 8)
        self.liste_recettes.append(etapes)

class Salade(Entree):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Laver la salade", 1)
        etapes[2] = ("Couper les légumes", 3)
        etapes[3] = ("Mélanger avec la vinaigrette", 2)
        self.liste_recettes.append(etapes)

class Frites(Entree):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Faire frire les pommes de terre", 5)
        etapes[2] = ("Préparer la mayonnaise", 2)
        etapes[3] = ("Assaisonner les frites", 1)
        self.liste_recettes.append(etapes)

class Tartare(Entree):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Couper le saumon", 2)
        etapes[2] = ("Mélanger avec la sauce", 1)
        etapes[3] = ("Placer dans l'assiette", 1)
        self.liste_recettes.append(etapes)

class Gateau(Dessert):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Couper le gâteau", 1)
        etapes[2] = ("Couper les fruits", 2)
        etapes[3] = ("Servir la crème glacée", 1)
        self.liste_recettes.append(etapes)

class Sunday(Dessert):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Servir la crème glacée", 1)
        etapes[2] = ("Couper des fraises", 1)
        etapes[3] = ("Ajouter le fudge", 1)
        self.liste_recettes.append(etapes)

class Brownies(Dessert):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Réchauffer les brownies", 2)
        etapes[2] = ("Servir la crème glacée", 1)
        self.liste_recettes.append(etapes)

class Cafe(Boisson):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Remplir la cafetière", 1)
        etapes[2] = ("Laisser infuser le café", 4)
        self.liste_recettes.append(etapes)

class Limonade(Boisson):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Presser les citrons", 2)
        etapes[2] = ("Mélanger avec de l'eau et du sucre", 1)
        self.liste_recettes.append(etapes)

class JusPomme(Boisson):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        etapes = {}
        etapes[1] = ("Couper les pommes", 1)
        etapes[2] = ("Extraire le jus", 2)
        self.liste_recettes.append(etapes)