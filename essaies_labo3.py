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
        self.recettes_dejeuner = self.liste_recettes_dejeuner()
        self.recettes_diner = self.liste_recettes_diner()
        self.recettes_souper = self.liste_recettes_souper()
        self.recettes_entree = self.liste_recettes_entree()
        self.recettes_dessert = self.liste_recettes_dessert()
        self.recettes_boisson = self.liste_recettes_boisson()
    
    def liste_recettes_dejeuner(self):
        liste_dej = []
        # recette1
        liste_etapes = []
        liste_etapes.append(Etape("Faire cuire les oeufs", 4))
        liste_etapes.append(Etape("Réchauffer les pommes de terre", 2))
        liste_etapes.append(Etape("Couper les fruits", 2))
        liste_dej.append(Recette("Oeufs avec fruits et pomme de terre", liste_etapes))
        # recette2
        liste_etapes = []
        liste_etapes.append(Etape("Tremper le pain dans le mélange", 1))
        liste_etapes.append(Etape("Faire cuire dans la poèle", 4))
        liste_etapes.append(Etape("Couper les fruits", 2))
        liste_dej.append(Recette("Pain doré", liste_etapes))
        # recette3
        liste_etapes = []
        liste_etapes.append(Etape("Battre le mélange", 1))
        liste_etapes.append(Etape("Faire cuire dans la poèle", 5))
        liste_etapes.append(Etape("Couper les fruits", 2))
        liste_dej.append(Recette("Crêpes", liste_etapes))
        return liste_dej
    
    def liste_recettes_diner(self):
        liste_diner = []
        # recette1
        liste_etapes = []
        liste_etapes.append(Etape("Mettre les morceaux de poulet dans la chapelure", 2))
        liste_etapes.append(Etape("Faire frire le poulet", 5))
        liste_etapes.append(Etape("Réchauffer les pommes de terres", 2))
        liste_diner.append(Recette("Croquettes de poulet", liste_etapes))
        # recette2
        liste_etapes = []
        liste_etapes.append(Etape("Mettre le pain au four", 3))
        liste_etapes.append(Etape("Tartiner le pain", 1))
        liste_etapes.append(Etape("Servir la salade", 1))
        liste_diner.append(Recette("Sandwich au thon", liste_etapes))
        # recette3
        liste_etapes = []
        liste_etapes.append(Etape("Faire bouillir l'eau", 3))
        liste_etapes.append(Etape("Faire cuire les macaronis", 7))
        liste_etapes.append(Etape("Réchauffer la sauce", 2))
        liste_diner.append(Recette("Macaronis", liste_etapes))
        return liste_diner

    def liste_recettes_souper(self):
        liste_souper = []
        # recette1
        liste_etapes = []
        liste_etapes.append(Etape("Faire chauffer l'huile dans la poèle", 1))
        liste_etapes.append(Etape("Faire cuire le saumon", 5))
        liste_etapes.append(Etape("Réchauffer le riz", 2))
        liste_souper.append(Recette("Saumon", liste_etapes))
        # recette2
        liste_etapes = []
        liste_etapes.append(Etape("Faire frire les falafels", 5))
        liste_etapes.append(Etape("Réchauffer le pain pita", 2))
        liste_etapes.append(Etape("Garnir le pain avec les falafels", 2))
        liste_souper.append(Recette("Pita Falafel", liste_etapes))
        # recette3
        liste_etapes = []
        liste_etapes.append(Etape("Préparer la pâte", 3))
        liste_etapes.append(Etape("Garnir la pizza", 2))
        liste_etapes.append(Etape("Cuire la pizza", 8))
        liste_souper.append(Recette("Pizza végétarienne", liste_etapes))
        return liste_souper

    def liste_recettes_entree(self):
        liste_entrees = []
        # recette1
        liste_etapes = []
        liste_etapes.append(Etape("Laver la salade", 1))
        liste_etapes.append(Etape("Couper les légumes", 3))
        liste_etapes.append(Etape("Mélanger avec la vinaigrette", 2))
        liste_entrees.append(Recette("Salade du chef", liste_etapes))
        # recette2
        liste_etapes = []
        liste_etapes.append(Etape("Faire frire les pommes de terre", 5))
        liste_etapes.append(Etape("Préparer la mayonnaise", 2))
        liste_etapes.append(Etape("Assaisonner les frites", 1))
        liste_entrees.append(Recette("Frites", liste_etapes))
        # recette3
        liste_etapes = []
        liste_etapes.append(Etape("Couper le saumon", 2))
        liste_etapes.append(Etape("Mélanger avec la sauce", 1))
        liste_etapes.append(Etape("Placer dans l'assiette", 1))
        liste_entrees.append(Recette("Tartare de saumon", liste_etapes))
        return liste_entrees
    
    def liste_recettes_dessert(self):
        liste_desserts = []
        # recette1
        liste_etapes = []
        liste_etapes.append(Etape("Couper le gâteau", 1))
        liste_etapes.append(Etape("Couper les fruits", 2))
        liste_etapes.append(Etape("Servir la crème glacée", 1))
        liste_desserts.append(Recette("Gâteau au chocolat", liste_etapes))
        # recette2
        liste_etapes = []
        liste_etapes.append(Etape("Servir la crème glacée", 1))
        liste_etapes.append(Etape("Couper des fraises", 1))
        liste_etapes.append(Etape("Ajouter le fudge", 1))
        liste_desserts.append(Recette("Sunday", liste_etapes))
        # recette3
        liste_etapes = []
        liste_etapes.append(Etape("Réchauffer les brownies", 2))
        liste_etapes.append(Etape("Servir la crème glacée", 1))
        liste_desserts.append(Recette("Brownies", liste_etapes))
        return liste_desserts
    
    def liste_recettes_boisson(self):
        liste_boissons = []
        # recette1
        liste_etapes = []
        liste_etapes.append(Etape("Remplir la cafetière", 1))
        liste_etapes.append(Etape("Laisser infuser le café", 4))
        liste_boissons.append(Recette("Café", liste_etapes))
        # recette2
        liste_etapes = []
        liste_etapes.append(Etape("Presser les citrons", 2))
        liste_etapes.append(Etape("Mélanger avec de l'eau et du sucre", 1))
        liste_boissons.append(Recette("Limonade", liste_etapes))
        # recette3
        liste_etapes = []
        liste_etapes.append(Etape("Couper les pommes", 1))
        liste_etapes.append(Etape("Extraire le jus", 2))
        liste_boissons.append(Recette("Jus de pommes maison", liste_etapes))
        return liste_boissons