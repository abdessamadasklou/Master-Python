def convert_to_int(value) :
    resulta = int(value)
    return resulta

try :
    print(convert_to_int(23.9))
except ValueError :
    print("la coonvertion a echouee")