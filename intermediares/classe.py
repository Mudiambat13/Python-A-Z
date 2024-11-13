class Voiture:
    def __init__(self, nom, carburant, serie, moteur):
        self.nom = nom
        self.carburant = carburant
        self.serie = serie
        self.moteur = moteur

    def presentation(self):
        print(f"Ce véhicule est de la marque {self.nom}, de série {self.serie}, ayant un moteur {self.moteur} fonctionnant au {self.carburant}.")

# Création d'une instance de la classe Voiture
hilux = Voiture('Toyota_Hilux', 'Diesel', 2022, 'V6')

# Appel de la méthode presentation sur l'instance
hilux.presentation() 