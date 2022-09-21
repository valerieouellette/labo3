from datetime import datetime

class Repas:
    def __init__(self) -> None:
        self.liste_recette = []
        self.recette()
        self.temps_debut = 0
    
    def recette(self):
        pass
    
    def get_time(self):
        prise_donnee = False
        while not prise_donnee:
            print("Voulez-vous la commmande pour:")
            options = {}
            options[1] = "Maintenant"
            options[2] = "Une heure particulière"
            for numero, option in options.items():
                print(f"{numero}) {option}")
            choix = input("Choix: ")
            if choix == "1":
                now = now.time()
                self.temps_debut = (now[0], now[1])
                prise_donnee = True
            elif choix == "2":
                heure = input("Entrez heure désirée (en format 00:00): ")
                heure = heure.split(":")
                self.temps_debut = (heure[0], heure[1])
                prise_donnee = True
            else:
                print("Choix invalide, recommencez")

    def __add__(self, repas2):
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
        self.liste_recette.append("Faire cuire les oeufs", 4)
        self.liste_recette.append("Réchauffer les pommes de terre", 2)
        self.liste_recette.append("Couper les fruits", 2)

class PainDore(Dejeuner):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Tremper le pain dans le mélange", 1)
        self.liste_recette.append("Faire cuire dans la poèle", 4)
        self.liste_recette.append("Couper les fruits", 2)
        
class Crepes(Dejeuner):
    def __init__(self) -> None:
        self.__init__()
    
    def recette(self):
        self.liste_recette.append("Battre le mélange", 1)
        self.liste_recette.append("Faire cuire dans la poèle", 5)
        self.liste_recette.append("Couper les fruits", 2)

class CroquettePoulet(Diner):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Mettre les morceaux de poulet dans la chapelure", 2)
        self.liste_recette.append("Faire frire le poulet", 5)
        self.liste_recette.append("Réchauffer les pommes de terres", 2)

class SandwichThon(Diner):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Mettre le pain au four", 3)
        self.liste_recette.append("Tartiner le pain", 1)
        self.liste_recette.append("Servir la salade", 1)

class Macaronis(Diner):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Faire bouillir l'eau", 3)
        self.liste_recette.append("Faire cuire les macaronis", 7)
        self.liste_recette.append("Réchauffer la sauce", 2)

class Saumon(Souper):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Faire chauffer l'huile dans la poèle", 1)
        self.liste_recette.append("Faire cuire le saumon", 5)
        self.liste_recette.append("Réchauffer le riz", 2)

class PitaFalafel(Souper):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Faire frire les falafels", 5)
        self.liste_recette.append("Réchauffer le pain pita", 2)
        self.liste_recette.append("Garnir le pain avec les falafels", 2)

class PizzaVege(Souper):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Préparer la pâte", 3)
        self.liste_recette.append("Garnir la pizza", 2)
        self.liste_recette.append("Cuire la pizza", 8)

class Salade(Entree):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Laver la salade", 1)
        self.liste_recette.append("Couper les légumes", 3)
        self.liste_recette.append("Mélanger avec la vinaigrette", 2)

class Frites(Entree):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Faire frire les pommes de terre", 5)
        self.liste_recette.append("Préparer la mayonnaise", 2)
        self.liste_recette.append("Assaisonner les frites", 1)

class Tartare(Entree):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Couper le saumon", 2)
        self.liste_recette.append("Mélanger avec la sauce", 1)
        self.liste_recette.append("Placer dans l'assiette", 1)

class Gateau(Dessert):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Couper le gâteau", 1)
        self.liste_recette.append("Couper les fruits", 2)
        self.liste_recette.append("Servir la crème glacée", 1)

class Sunday(Dessert):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Servir la crème glacée", 1)
        self.liste_recette.append("Couper des fraises", 1)
        self.liste_recette.append("Ajouter le fudge", 1)

class Brownies(Dessert):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Réchauffer les brownies", 2)
        self.liste_recette.append("Servir la crème glacée", 1)

class Cafe(Boisson):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Remplir la cafetière", 1)
        self.liste_recette.append("Laisser infuser le café", 4)

class Limonade(Boisson):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Presser les citrons", 2)
        self.liste_recette.append("Mélanger avec de l'eau et du sucre", 1)

class JusPomme(Boisson):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append("Couper les pommes", 1)
        self.liste_recette.append("Extraire le jus", 2)


class Restaurant:
    def __init__(self) -> None:
        pass

    def menu(self):
        pass
