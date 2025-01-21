def process_input(num):
    intnum=int(num)
    return 10/intnum
try :
    print(process_input("rr"))
except ValueError :
    print("la convertion a echouee")

except ZeroDivisionError :
    print("vous avez fait une division par zero")
