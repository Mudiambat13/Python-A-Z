prix_ht = float(input("Entrez le prix HT: "))
taux_tva = float(input("Entrez le taux de TVA (en %) : "))

tva = prix_ht * taux_tva / 100
prix_ttc = prix_ht + tva 

print("Le prix TTC est de", prix_ttc)