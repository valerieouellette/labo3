import datetime

class Repas:
    def __init__(self) -> None:
        self.nom = ""
        self.liste_recette = []
        self.temps_debut = 0
        self.temps_fin = 0
        self.recette()
    
    def __str__(self):
        recette = ""
        recette += self.nom + ": \n"
        for etape in self.liste_recette:
            recette += f"{etape[0]} ({etape[1]}min)" + "\n"
        return recette
    
    def recette(self):
        pass

#le repas avec le temps max définit le debut et fin préparation
#placer ensuite les étapes pour finir en même temps
    def __add__(self, repas2):
        pass
                    
class Oeufs(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Oeufs"
        self.temps_execution = 8
    
    def recette(self):
        self.liste_recette.append(("Faire cuire les oeufs", 4))
        self.liste_recette.append(("Réchauffer les pommes de terre", 2))
        self.liste_recette.append(("Couper les fruits", 2))

class PainDore(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Pain doré"
        self.temps_execution = 7
    
    def recette(self):
        self.liste_recette.append(("Tremper le pain dans le mélange", 1))
        self.liste_recette.append(("Faire cuire dans la poèle", 4))
        self.liste_recette.append(("Couper les fruits", 2))
        
class Crepes(Repas):
    def __init__(self) -> None:
        self.__init__()
        self.nom = "Crêpes"
        self.temps_execution = 8
    
    def recette(self):
        self.liste_recette.append(("Battre le mélange", 1))
        self.liste_recette.append(("Faire cuire dans la poèle", 5))
        self.liste_recette.append(("Couper les fruits", 2))

class CroquettePoulet(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Croquettes de poulet"
        self.temps_execution = 9
    
    def recette(self):
        self.liste_recette.append(("Mettre les morceaux de poulet dans la chapelure", 2))
        self.liste_recette.append(("Faire frire le poulet", 5))
        self.liste_recette.append(("Réchauffer les pommes de terres", 2))

class SandwichThon(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Sandwich au thon"
        self.temps_execution = 5
    
    def recette(self):
        self.liste_recette.append(("Mettre le pain au four", 3))
        self.liste_recette.append(("Tartiner le pain", 1))
        self.liste_recette.append(("Servir la salade", 1))

class Macaronis(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Macaronis"
        self.temps_execution = 12
    
    def recette(self):
        self.liste_recette.append(("Faire bouillir l'eau", 3))
        self.liste_recette.append(("Faire cuire les macaronis", 7))
        self.liste_recette.append(("Réchauffer la sauce", 2))

class Saumon(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Saumon"
        self.temps_execution = 8
    
    def recette(self):
        self.liste_recette.append(("Faire chauffer l'huile dans la poèle", 1))
        self.liste_recette.append(("Faire cuire le saumon", 5))
        self.liste_recette.append(("Réchauffer le riz", 2))

class PitaFalafel(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Pita Falafel"
        self.temps_execution = 9
    
    def recette(self):
        self.liste_recette.append(("Faire frire les falafels", 5))
        self.liste_recette.append(("Réchauffer le pain pita", 2))
        self.liste_recette.append(("Garnir le pain avec les falafels", 2))

class PizzaVege(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Pizza Vege"
        self.temps_execution = 13
    
    def recette(self):
        self.liste_recette.append(("Préparer la pâte", 3))
        self.liste_recette.append(("Garnir la pizza", 2))
        self.liste_recette.append(("Cuire la pizza", 8))

class Salade(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Salade"
        self.temps_execution = 6
    
    def recette(self):
        self.liste_recette.append(("Laver la salade", 1))
        self.liste_recette.append(("Couper les légumes", 3))
        self.liste_recette.append(("Mélanger avec la vinaigrette", 2))

class Frites(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Frites"
        self.temps_execution = 8
    
    def recette(self):
        self.liste_recette.append(("Faire frire les pommes de terre", 5))
        self.liste_recette.append(("Préparer la mayonnaise", 2))
        self.liste_recette.append(("Assaisonner les frites", 1))

class Tartare(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Tartare"
        self.temps_execution = 4
    
    def recette(self):
        self.liste_recette.append(("Couper le saumon", 2))
        self.liste_recette.append(("Mélanger avec la sauce", 1))
        self.liste_recette.append(("Placer dans l'assiette", 1))

class Gateau(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Gâteau"
        self.temps_execution = 4
    
    def recette(self):
        self.liste_recette.append(("Couper le gâteau", 1))
        self.liste_recette.append(("Couper les fruits", 2))
        self.liste_recette.append(("Servir la crème glacée", 1))

class Sunday(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Sunday"
        self.temps_execution = 3
    
    def recette(self):
        self.liste_recette.append(("Servir la crème glacée", 1))
        self.liste_recette.append(("Couper des fraises", 1))
        self.liste_recette.append(("Ajouter le fudge", 1))

class Brownies(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Brownies"
        self.temps_execution = 3
    
    def recette(self):
        self.liste_recette.append(("Réchauffer les brownies", 2))
        self.liste_recette.append(("Servir la crème glacée", 1))

class Cafe(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Café"
        self.temps_execution = 5
    
    def recette(self):
        self.liste_recette.append(("Remplir la cafetière", 1))
        self.liste_recette.append(("Laisser infuser le café", 4))

class Limonade(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Limonade"
        self.temps_execution = 3
    
    def recette(self):
        self.liste_recette.append(("Presser les citrons", 2))
        self.liste_recette.append(("Mélanger avec de l'eau et du sucre", 1))

class JusPomme(Repas):
    def __init__(self) -> None:
        super().__init__()
        self.nom = "Jus de pomme"
        self.temps_execution = 3
    
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
                heure = datetime.datetime.now()
                heure = (heure.hour, heure.minute)
                prise_donnee = True
                now = True
            elif choix == "2":
                heure = input("Entrez heure désirée (en format 00:00): ")
                heure = heure.split(":")
                heure = (int(heure[0]), int(heure[1]))
                prise_donnee = True
                now = False
            else:
                print("Choix invalide, recommencez")
        return heure, now
    
    @staticmethod
    def creation_repas(repas):
        repas = repas.replace(" ", "")
        if repas.lower() == "oeufs":
            return Oeufs()
        elif repas.lower() == "paindoré" or repas.lower() == "paindore":
            return PainDore()
        elif repas.lower() == "crêpes" or repas.lower() == "crepes":
            return Crepes()
        elif repas.lower() == "sandwichauthon":
            return SandwichThon()
        elif repas.lower() == "croquettesdepoulet":
            return CroquettePoulet()
        elif repas.lower() == "macaronis":
            return Macaronis()
        elif repas.lower() == "saumon":
            return Saumon()
        elif repas.lower() == "pitafalafel":
            return PitaFalafel()
        elif repas.lower() == "pizzavege":
            return PizzaVege()
        elif repas.lower() == "gateau" or repas.lower() == "gâteau":
            return Gateau()
        elif repas.lower() == "sunday":
            return Sunday()
        elif repas.lower() == "brownies":
            return Brownies()
        elif repas.lower() == "salade":
            return Salade
        elif repas.lower() == "frites":
            return Frites()
        elif repas.lower() == "tartaredesaumon":
            return Tartare()
        elif repas.lower() == "cafe" or repas.lower() == "café":
            return Cafe()
        elif repas.lower() == "limonade":
            return Limonade()
        elif repas.lower() == "jusdepomme":
            return JusPomme()

    @staticmethod
    def menu_utilisateur():
        liste_repas = []
        time, now = Restaurant.get_time()
        Restaurant.affichage_menu(time)
        commande = input("Entrez votre commande: ")
        commande = commande.split("+")
        for repas in commande:
            liste_repas.append(Restaurant.creation_repas(repas))
        for i in range(len(liste_repas)):
            print(str(liste_repas[i]))
            if i != (len(liste_repas) - 1):
                print(liste_repas[i] + liste_repas[i+1])
            
                

#Continuer l'implémentation du menu
#Additionner les repas


Restaurant.menu_utilisateur()
        


