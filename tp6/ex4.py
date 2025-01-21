class NegativeAgeError(Exception):
    pass
def set_age(age):
        if age < 0:
             raise NegativeAgeError("l'age est negatif.")
        else:
              print(age)
try:
      set_age(7)
except NegativeAgeError as e:
      print(e)
    
