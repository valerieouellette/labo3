from datetime import datetime

class Repas:
    def __init__(self) -> None:
        self.liste_recette = []
        self.temps_debut = 0
        self.temps_fin = 0
        self.recette()
    
    def __str__(self):
        recette = ""
        for etape in self.liste_recette:
            recette += f"{etape[0]} ({etape[1]}min)" + "\n"
        return recette
    
    def recette(self):
        pass

    def __add__(self, repas2):
        new_list = []
        for etape in self.liste_recette:
            for etape2 in repas2.liste_recette:
                if etape[1] > etape2[1]:
                    new_list.append(etape2)
                    new_list.append(etape)
                else:
                    new_list.append(etape)
                    new_list.append(etape2)
        repas = Repas()
        repas.liste_recette = new_list
        return repas
                    
class Oeufs(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Faire cuire les oeufs", 4))
        self.liste_recette.append(("Réchauffer les pommes de terre", 2))
        self.liste_recette.append(("Couper les fruits", 2))

class PainDore(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Tremper le pain dans le mélange", 1))
        self.liste_recette.append(("Faire cuire dans la poèle", 4))
        self.liste_recette.append(("Couper les fruits", 2))
        
class Crepes(Repas):
    def __init__(self) -> None:
        self.__init__()
    
    def recette(self):
        self.liste_recette.append(("Battre le mélange", 1))
        self.liste_recette.append(("Faire cuire dans la poèle", 5))
        self.liste_recette.append(("Couper les fruits", 2))

class CroquettePoulet(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Mettre les morceaux de poulet dans la chapelure", 2))
        self.liste_recette.append(("Faire frire le poulet", 5))
        self.liste_recette.append(("Réchauffer les pommes de terres", 2))

class SandwichThon(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Mettre le pain au four", 3))
        self.liste_recette.append(("Tartiner le pain", 1))
        self.liste_recette.append(("Servir la salade", 1))

class Macaronis(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Faire bouillir l'eau", 3))
        self.liste_recette.append(("Faire cuire les macaronis", 7))
        self.liste_recette.append(("Réchauffer la sauce", 2))

class Saumon(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Faire chauffer l'huile dans la poèle", 1))
        self.liste_recette.append(("Faire cuire le saumon", 5))
        self.liste_recette.append(("Réchauffer le riz", 2))

class PitaFalafel(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Faire frire les falafels", 5))
        self.liste_recette.append(("Réchauffer le pain pita", 2))
        self.liste_recette.append(("Garnir le pain avec les falafels", 2))

class PizzaVege(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Préparer la pâte", 3))
        self.liste_recette.append(("Garnir la pizza", 2))
        self.liste_recette.append(("Cuire la pizza", 8))

class Salade(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Laver la salade", 1))
        self.liste_recette.append(("Couper les légumes", 3))
        self.liste_recette.append(("Mélanger avec la vinaigrette", 2))

class Frites(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Faire frire les pommes de terre", 5))
        self.liste_recette.append(("Préparer la mayonnaise", 2))
        self.liste_recette.append(("Assaisonner les frites", 1))

class Tartare(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Couper le saumon", 2))
        self.liste_recette.append(("Mélanger avec la sauce", 1))
        self.liste_recette.append(("Placer dans l'assiette", 1))

class Gateau(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Couper le gâteau", 1))
        self.liste_recette.append(("Couper les fruits", 2))
        self.liste_recette.append(("Servir la crème glacée", 1))

class Sunday(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Servir la crème glacée", 1))
        self.liste_recette.append(("Couper des fraises", 1))
        self.liste_recette.append(("Ajouter le fudge", 1))

class Brownies(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Réchauffer les brownies", 2))
        self.liste_recette.append(("Servir la crème glacée", 1))

class Cafe(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Remplir la cafetière", 1))
        self.liste_recette.append(("Laisser infuser le café", 4))

class Limonade(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Presser les citrons", 2))
        self.liste_recette.append(("Mélanger avec de l'eau et du sucre", 1))

class JusPomme(Repas):
    def __init__(self) -> None:
        super().__init__()
    
    def recette(self):
        self.liste_recette.append(("Couper les pommes", 1))
        self.liste_recette.append(("Extraire le jus", 2))


class Restaurant:

    LISTE_DEJEUNER = ["Oeufs", "Pain doré", "Crêpes"]
    LISTE_DINER = ["Sandwich au thon", "Croquettes de poulet", "Macaronis"]
    LISTE_SOUPER = ["Saumon", "Pita Falafel", "Pizza vege"]
    LISTE_DESSERTS = ["Gâteau", "Sunday", "Brownies"]
    LISTE_ENTREES = ["Salade", "Frites", "Tartare de saumon"]
    LISTE_BOISSONS = ["Café", "Limonade", "Jus de pomme"]

    HEURES_DEJEUNER = (6, 12)
    HEURES_DINER = (11, 15)
    HEURES_SOUPER = (15, 21)
    HEURES_ENTREE = (6, 21)
    HEURES_DESSERT = (11, 21)
    HEURES_BOISSON = (6, 21)

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def affichage_menu(heure):
        heure = heure[0]
        menu = ""
        if Restaurant.HEURES_DEJEUNER[0] <= heure < Restaurant.HEURES_DEJEUNER[1]:
            menu += "\n Déjeuner: \n"
            for repas in Restaurant.LISTE_DEJEUNER:
                menu += repas + "\n"
        if Restaurant.HEURES_DINER[0] <= heure < Restaurant.HEURES_DINER[1]:
            menu += "\n Dîner: \n"
            for repas in Restaurant.LISTE_DINER:
                menu += repas + "\n"
        if Restaurant.HEURES_SOUPER[0] <= heure < Restaurant.HEURES_SOUPER[1]:
            menu += "\n Souper: \n"
            for repas in Restaurant.LISTE_SOUPER:
                menu += repas + "\n"
        if Restaurant.HEURES_ENTREE[0] <= heure < Restaurant.HEURES_ENTREE[1]:
            menu += "\n Entrées: \n"
            for repas in Restaurant.LISTE_ENTREES:
                menu += repas + "\n"
        if Restaurant.HEURES_DESSERT[0] <= heure < Restaurant.HEURES_DESSERT[1]:
            menu += "\n Desserts: \n"
            for repas in Restaurant.LISTE_DESSERTS:
                menu += repas + "\n"
        if Restaurant.HEURES_BOISSON[0] <= heure < Restaurant.HEURES_BOISSON[1]:
            menu += "\n Boissons: \n"
            for repas in Restaurant.LISTE_BOISSONS:
                menu += repas + "\n"
        else:
            menu += "Nous sommes fermés. Revenez demain!"
        print(menu)
    
    @staticmethod
    def get_time():
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
                time = (now[0], now[1])
                prise_donnee = True
                now = True
            elif choix == "2":
                heure = input("Entrez heure désirée (en format 00:00): ")
                heure = heure.split(":")
                time = (int(heure[0]), int(heure[1]))
                prise_donnee = True
                now = False
            else:
                print("Choix invalide, recommencez")
        return time, now
    
    @staticmethod
    def menu_utilisateur():
        time, now = Restaurant.get_time()
        Restaurant.affichage_menu(time)


Restaurant.menu_utilisateur()
        


