my_dict = {
     "cle_1": "valeur_1",
     "cle_2": "valeur_2",
     "cle_3": "valeur_3",
     "cle_4": "valeur_4",
}
print(my_dict)
print(my_dict.keys())
# print dictionary keys

print(my_dict.values())
# print dictionary values

for key in my_dict.keys():
     for value in my_dict.values():
         print(key, value)
# print dictionary keys and values