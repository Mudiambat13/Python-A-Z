annee = int(input("Entrez une année : "))

if annee % 4 == 0 and annee % 100 != 0:
  print(annee, "est une année bissextile")
elif annee % 400 == 0:
  print(annee, "est une année bissextile")
else:
  print(annee, "n'est pas une année bissextile")