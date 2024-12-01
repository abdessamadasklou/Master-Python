def compte_occurences(liste) :
    d={}
    for mot in liste :
        if mot in d:
            d[mot]+=1
        else :
            d[mot]=1
    return d
print(compte_occurences(['abd',3,4,3,'abd','abd']))