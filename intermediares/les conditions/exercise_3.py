a = int(input("Entrez a: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))

if a > b and a > c:
  print("a est le plus grand")
elif b > a and b > c:
  print("b est le plus grand")
else:
  print("c est le plus grand")