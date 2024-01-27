from math import sqrt

"""

Écrire en Python une classe «Rectangle» ayant deux variables « a » et « b »
et une fonction membre « surface() » qui retournera la surface du rectangle.

"""

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def surface(self):
        return self.a * self.b


"""

Écrire en Python une classe « Somme » ayant deux variables « n1 » et « n2 » et 
une fonction membre « som() » qui calcule la somme. Dans la méthode principale 
main demandez à l’utilisateur d’entrez deux entiers et passez-les au constructeur
par défaut de la classe « Somme » et afficher le résultat de l’addition des deux nombres.

"""


class Somme:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def som(self):
        return self.a+self.b


"""

Écrire classe Python appelée « Etudiant » avec les membres suivant :
nom : (de type char),
note1, note2 : (de type float)
calc_moy() : calcule la note moyenne.
afficher () : affiche le nom et la note moyenne.
Le programme principal (main) demande à l’utilisateur d’entrer le nom 
et les notes d'un étudiant. et affiche leur nom et la note moyenne.

"""

class Etudiant:
    def __init__(self, nom, note1, note2):
        self.nom = nom
        self.note1 = note1
        self.note2 = note2

    def calc_moy(self):
        return (self.note1 + self.note2) / 2

    def __str__(self):
        return f"{self.nom} a une moyenne de {Etudiant.calc_moy(self)}"

    def afficher(self):
        return f"{self.nom} a une moyenne de {Etudiant.calc_moy(self)}"


"""
Réaliser en Python  une classe point permettant de manipuler un point d'un plan.on prévoira :

1) un point est définit par ses coordonnées x et y (des membres privés)

2) les constructeurs 

3) une fonction membre déplace effectuant une translation définie par ses deux arguments dx et dy (double)

4)une fonction membre affiche se contentant d'afficher les coordonnées cartésiennes du point.

5)une fonction membre saisir se contentant de saisir les coordonnées cartésiennes du point.

6)une fonction membre distance effectuant calculant la distance entre deux point.

7)une fonction membre milieu donnant le milieu d'un segment.

8)un petit programme d'essai (main) gérant la classe point.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self,a):
        return self.x = a

    def set_y(self,b):
        return self.y = b


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


    def membreDeplace(self, dx, dy):
        self.set_x(self.get_x + dx)
        self.set_y(self.get_y + dy)

    def membreAffiche(self):
        print(f"({self.get_x(),self.get_y()}")

    def saisir(self):
        self.set_x = input("Entrer x: \n")
        self.set_y = input("Entrer y: \n")

    def distance(self, a):
        a1 = (self.get_x() - a.get_x()) * (self.get_x() - a.get_x())
        a2 = (self.get_y() - a.get_y()) * (self.get_y() - a.get_y())

        r = sqrt(a1+a2)

        return r




if __name__ == "__main__":
    """
    Test Pour l'exercice 1
   

    r = Rectangle(4, 5)

    print(f"La surface est {Rectangle.surface(r)}")
    
    """

    """
    #Test Pour l'exercice 2


    r = Somme(4,5)

    print(f"La somme est {Somme.som(r)}")

    """


    """
    #Test Pour l'exercice 3


    e = Etudiant("Mouhamedoune ", 15, 18)

    #print(e)

    print(Etudiant.afficher(e))

    """

