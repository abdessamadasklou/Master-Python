def safe_division(a,b):
    resulta=a/b
    return resulta
try :
    resulta= safe_division(1,2)
except ZeroDivisionError :
    print("vous avez fait une division par zero")

else:
    print(f"la division a ete effectuee avec succes: {resulta}")
finally:
    print("la fonction est terminé.")