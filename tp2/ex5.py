class Animal :
    def faire_de_bruit(self):
        return "cet animal fait un bruit."
class chien(Animal):
    def faire_de_bruit(self): 
        return "Le chien aboie WOOF WOOF"
class Chat(Animal):
    def faire_de_bruit(self): 
        return "Le chat miaule MIAO MIAO"
    
animal = Animal()
chien = chien()
chat = Chat()

print(animal.faire_de_bruit())
print(chien.faire_de_bruit())
print(chat.faire_de_bruit())