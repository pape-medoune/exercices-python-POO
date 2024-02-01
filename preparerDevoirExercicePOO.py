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

    def get_x(self):
       return self.x

    def set_x(self,x):
        self.x=x


    def get_y(self):
        return self.y


    def set_y(self, y):
        self.y = y

    def membre(self, dx, dy):
        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)


    def afficherCoordonnee(self):
       return f"({self.get_x()} , {self.get_y()})"

    def __str__(self):
       return f"({self.get_x()} , {self.get_y()})"

    def saisie(self):
        a1 = input("Donnez x:\n")
        a2 = input("Donnez y:\n")

        self.set_x(a1)
        self.set_y(a2)


    def calculeDistance(self, p):
        a1 = (self.get_x() - p.get_x()) * (self.get_x() - p.get_x())
        a2 = (self.get_y() - p.get_y()) * (self.get_y() - p.get_y())

        return sqrt(a1 + a2)


    def milieuSegment(self, p):
        a1 = Point(0 ,0)

        a1.x = (self.get_x() + p.get_x()) / 2
        a1.y = (self.get_y() + p.get_y()) / 2

        return a1


"""

Écrire un programme en Python qui simule la gestion d’un simple compte bancaire. 
Le compte est créé avec un solde initial. Il est possible de déposer et de retirer 
des fonds, d’ajouter des intérêts et de connaître le solde actuel. Cela devrait 
être implémenté dans une classe nommée Account qui comprend:


1) Un constructeur par défaut qui met le solde initial à zéro.
2) Un constructeur qui accepte une balance initial comme paramètre.
3) Une fonction getBalance qui renvoie le solde actuel.
4) Une méthode deposer pour déposer un montant spécifié.
5) Une méthode retirer pour retirer un montant spécifié.
6) Une méthode ajouter_Interet pour ajouter de l’intérêt au compte.
La méthode  ajouter_Interet  prend le taux d’intérêt comme paramètre 
et modifie le solde du compte en solde * (1 + taux d’intérêt).

"""

class Account:
    def __init__(self, solde):
        self.solde = 0


    def getBalance(self):
        return self.solde

    def deposer(self, montant):
        self.solde += montant

        return self.solde

    def retirer(self, montant):
        self.solde -= montant

        return self.solde

    def ajouter_interet(self, taux):
        self.solde *= (1+(taux/100))

        return self.solde

"""
Créer en Python une classe appelée Temps, qui a des membres de type int 
tels que heures, minutes et secondes.(rendez-les private)
1) Un constructeur doit initialiser ces données à 0
2) Un autre constructeur devrait l’initialiser à des valeurs fixes.
3) Une fonction membre devrait l’afficher, au format 17h 59min 59s.
4) Une autre fonction pour renvoyer les données de chaque membre nommez-les getheurs, 
getMin et getSec
5) Une fonction membre doit ajouter deux objets de type Temps passé en arguments.

"""


class temps:
    def __init__(self, h=0, m=0, s=0):
        self._h = h
        self._m = m
        self._s = s

    def setTemps(self, h, m, s):
        self._h = h
        self._m = m
        self._s = s

    def set_h(self, a):
        self._h = a

    def get_h(self):
        return self._h

    def set_m(self, a):
        self._m = a

    def get_m(self):
        return self._m

    def set_s(self, a):
        self._s = a

    def get_s(self):
        return self._s

    def membre(self):
        print(f"{self.get_h()}h {self.get_m()}m {self.get_s()}s")

    def ajoutTemps(self, t1, t2):
        self._s = t1.get_s() + t2.get_s()
        self._m = t1.get_m() + t2.get_m() + self._s / 60
        self._h = t1.get_h() + t2.get_h() + self._m / 60
        self._s = self._s % 60
        self._m = self._m % 60


"""

Écrire en Python un programme utilisant une classe rectangle
dont le constructeur prend deux paramètres, largeur et hauteur
et qui offre les fonctions suivantes :

1) calcul du périmètre

2) calcul de la surface

3)  affichage

ainsi que les accesseurs et mutateurs triviaux (lecture
et modification de la largeur et de la hauteur).

"""
class Rectangle:
    def __init__(self, longueur, largeur, hauteur):
        self.longueur = longueur
        self.largeur  = largeur
        self.hauteur = hauteur

    def set_longueur(self, a):
        self.longueur = a

    def get_longueur(self):
        return self.longueur

    def set_largeur(self, a):
        self.largeur = a

    def get_largeur(self):
        return self.largeur

    def set_hauteur(self, a):
        self.hauteur = a

    def get_hauteur(self):
        return self.hauteur
    def perimetre(self):
        return (self.get_longueur() +self.get_largeur()) /2

    def surface(self):
        return self.get_longueur() * self.get_largeur()

    def affichage(self):
        print(f"La figure rectangle de dimension l = {self.get_longueur()} , L = {self.get_largeur()} et de h = {self.get_hauteur()} \n à pour perimetre {self.perimetre()} et pour surface {self.surface()}")


"""
Écrivez un programme en Python qui définit une classe appelée Forme
avec un constructeur qui donne de la valeur à la largeur(x) et à la hauteur(y). 
Définir la méthode aire() dans les deux sous-classes Triangle et Rectangle, 
qui calculent l’aire. Dans la méthode principale main, définissez deux variables, 
un triangle et un rectangle, puis appelez la fonction aire() dans ces deux variables.

Notez que:

 l’aire du triangle est = largeur * hauteur / 2 

l’aire du rectangle est = largeur * hauteur.
"""
class Forme:
    def __init__(self, hauteur=0, largeur=0):
        self.largeur = largeur
        self.hauteur = hauteur

class Triangle(forme):
    def __init__(self, hauteur=0, largeur=0):
        Forme.__init__(self, hauteur, largeur)

    def aire(self):
        return (self.hauteur * self.largeur)/2


class Rectangle(forme):
    def __init__(self, hauteur=0, largeur=0):
        Forme.__init__(self, hauteur, largeur)

    def aire(self):
        return self.hauteur * self.largeur


class RectangleP:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur


    def perimetre(self):
        return ((self.longueur + self.largeur)*2)

    def aire(self):
        return self.longueur * self.largeur


    def get_largeur(self):
        return self.largeur

    def get_longueur(self):
        return self.largeur

    def set_largeur(self, a):
        self.largeur = a

    def set_longueur(self, a):
        self.longueur = a

class Parallelepipede(RectangleP):
    def __init__(self, largeur ,longueur, hauteur):
        RectangleP.__init__(self, largeur, longueur)
        self.hauteur = hauteur


    def Volume(self):
        return self.get_largeur() * self.get_longueur() * self.hauteur




class CompteBancaire:
    



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

    """

    #Test Pour l'exercice 4


    p = Point(4, -5)

    o = Point(2, 6)

    print(p)
    print(p.afficherCoordonnee())

    print(o)
    print(o.afficherCoordonnee())

    c = p.milieuSegment(o)

    print(f"{(c.get_x() , c.get_y())}")


    """
