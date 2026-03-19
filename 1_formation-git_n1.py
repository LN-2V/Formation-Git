print ("Branch du jardin")

class Terrain:
    def __init__(self, jardiniers, arbres):
        self.jardiniers = jardiniers
        self.arbres = arbres
    
    def afficher(self):
        print(self.jardiniers, self.arbres)


variable = Terrain("Jean", "Chêne")

variable.afficher()


