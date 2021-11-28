from turtle import*
from random import choice, randint


class Global:
    def __init__(self):
        pass

    def rectangle(self, n, l, L):
        """dessine un rectangle par récursivité
        l : largeur
        L : longueur"""  
        forward(l)
        right(90)
        forward(L)
        right(90)
        if n == 0:
            pass
        else:
            self.rectangle(n-1, l, L)
        
    def demi_cercle(self, taille, sens):
        """dessine un demi-cercle
        taille : taille du demi-cercle
        sens : sens du demi-cercle
            => r = doite
            => l = gauche"""
        if sens == "r":
            for x in range(180):
                forward(taille)
                right(1)
        elif sens == "l":
            for x in range(180):
                forward(taille)
                left(1)
                
                
class Ciel:
    def __init__(self):
        self.g = Global()
    
    def nuage(self, taille):
        """dessine un nuage par récursivité
        taille : taille du nuage"""
        if taille == 0:
            pass
        else:
            self.g.demi_cercle(1, "r")
            right(-90)
            self.nuage(taille-1)
            
            
class Mer:
    def __init__(self):
        pass
    
    def zigzag(self, nbr, longueur, a):
        """dessine des zigzags par récursivité
        nbr : nombre de zigzag
        longueur : longueur du premier zigzag
        a : l'écart entre les longueurs"""
        forward(longueur)
        goto(-longueur/2, a)
        if nbr == 0:
            pass
        else:
            self.zigzag(nbr-1, longueur/1.25, a-15)
            
            
class Palmier:
    def __init__(self):
        self.g = Global()
    
    def tron(self, taille, l, x, y):
        """dessine un tron par récursivité
        taille : nombre de rectangle formant le tron
        l : longueur du tron
        x : coordonnée en x
        y : coordonnée en y"""
        if taille == 0:
            pass
        else:
            up()
            goto(x, y)
            down()
            color('#9B6917')
            begin_fill()
            self.g.rectangle(1, l, 75)
            end_fill()
            a = randint(0, 10)
            self.tron(taille-1, l-20, x+a, y+75)   
        
    def feuille(self, n):
        """dessine une feuille par récursivité"""
        taille_f = [1, 1.5, 2]
        color('#179B23')
        begin_fill()
        if n == 0:
            pass
        elif n == 1:
            setheading(90)
            a = choice(taille_f)
            self.g.demi_cercle(a, "l")
            left(90)
            forward(115*a)
            end_fill()
            self.feuille(n-1)
        else:
            a = choice(taille_f)
            self.g.demi_cercle(a, "r")
            right(90)
            forward(115*a)
            end_fill()
            self.feuille(n-1)
        

class Plage:
    def __init__(self):
        self.g = Global()
    
    def serviette(self, nbr):
        """dessine une serviette récursive
        nbr : nombre de ligne"""
        couleur = ["#9B3F17", "#89179B", "#173D9B", "#29DCC3", "#AEDC29", "#000000", "#C8862C", "#B998F7"]
        if nbr == 0:
            pass
        else:
            color(choice(couleur))
            begin_fill()
            self.g.rectangle(1, 100, 35)
            right(90)
            forward(35)
            left(90)
            end_fill()
            self.serviette(nbr-1)       


class Neige:
    def __init__(self):
        pass
    
    def CourbeKoch(self, n,cote):
        if n == 0:
            forward(cote)
        else:
            self.CourbeKoch(n-1,cote/3)
            left(60)
            self.CourbeKoch(n-1,cote/3)
            right(120)
            self.CourbeKoch(n-1,cote/3)
            left(60)
            self.CourbeKoch(n-1,cote/3)
            
    def neige(self, flocon, x, y):
        """dessine de la neige en récursivité
        flocon : nombre de flocon
        x : coordonnée en x
        y : coordonnée en y"""
        if flocon == 0:
            pass
        else:
            up()
            goto(x, y)
            down()
            color('#FFFFFF')
            begin_fill()
            n = 3
            for i in range(n):
                self.CourbeKoch(3,100)
                left(360/n)
            end_fill()
            self.neige(flocon-1, randint(-300, 300), randint(-300, 300))   
