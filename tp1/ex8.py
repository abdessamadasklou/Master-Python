def somme_varargs(*args):
    somme = 0
    for i in args:
        somme += i
    return somme
print(somme_varargs(1, 2, 3))   
print(somme_varargs(4, 5, 6, 7)) 
