def fusionner_dicts(dict1, dict2):
    resultat = dict1.copy() 
    for key in dict2:
        if key in resultat:
            resultat[key] += dict2[key]  
        else:
            resultat[key] = dict2[key]  
    return resultat
dict1 = {'a': 3, 'b': 4, 'c': 5}
dict2 = {'b': 6, 'c': 2, 'd': 4}
print(fusionner_dicts(dict1, dict2))  
