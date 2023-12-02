1.append(x): Ajoute un élément à la fin de la liste.
`my_list = [1, 2, 3]`
`my_list.append(4)`
`print(my_list)`  `# Output: [1, 2, 3, 4]`

2.extend(iterable): Étend la liste en ajoutant tous les éléments de l'itérable fourni.
'my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]`

3.insert(i, x): Insère un élément à une position spécifique.

`my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]`

4.remove(x): Supprime le premier élément de la liste ayant la valeur spécifiée.

`my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]`

5.pop([i]): Supprime et renvoie l'élément à la position donnée (par défaut, le dernier élément).

`my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(my_list)        # Output: [1, 3]`

print(popped_element)  # Output: 2`

6.index(x): Renvoie l'indice du premier élément ayant la valeur spécifiée.

`my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1`

7.count(x): Renvoie le nombre d'occurrences de la valeur spécifiée.

`my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2`

8.sort(): Trie les éléments de la liste.

`my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 9]`

9.reverse(): Inverse l'ordre des éléments de la liste.

`my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]`