from turtle import*
from random import choice, randint
bgcolor("black")
setup(950, 800)
title("Plage Récursive")
speed(10)
shape('turtle')

def rectangle(n, l, L):
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
        rectangle(n-1, l, L)
        

def demi_cercle(taille, sens):
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
        

def zigzag(nbr, longueur, a):
    """dessine des zigzags par récursivité
    nbr : nombre de zigzag
    longueur : longueur du premier zigzag
    a : l'écart entre les longueurs"""
    forward(longueur)
    goto(-longueur/2, a)
    if nbr == 0:
        pass
    else:
        zigzag(nbr-1, longueur/1.25, a-15)

     
def nuage(taille):
    """dessine un nuage par récursivité
    taille : taille du nuage"""
    if taille == 0:
        pass
    else:
        demi_cercle(1, "r")
        right(-90)
        nuage(taille-1)
        

def tron(taille, l, x, y):
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
        rectangle(1, l, 75)
        end_fill()
        a = randint(0, 10)
        tron(taille-1, l-20, x+a, y+75)
        
        
def feuille(n):
    """dessine une feuille par récursivité"""
    taille_f = [1, 1.5, 2]
    color('#179B23')
    begin_fill()
    if n == 0:
        pass
    elif n == 1:
        setheading(90)
        a = choice(taille_f)
        demi_cercle(a, "l")
        left(90)
        forward(115*a)
        end_fill()
        feuille(n-1)
    else:
        a = choice(taille_f)
        demi_cercle(a, "r")
        right(90)
        forward(115*a)
        end_fill()
        feuille(n-1)
        

def serviette(nbr):
    """dessine une serviette récursive
    nbr : nombre de ligne"""
    couleur = ["#9B3F17", "#89179B", "#173D9B", "#29DCC3", "#AEDC29", "#000000", "#C8862C", "#B998F7"]
    if nbr == 0:
        pass
    else:
        color(choice(couleur))
        begin_fill()
        rectangle(1, 100, 35)
        right(90)
        forward(35)
        left(90)
        end_fill()
        serviette(nbr-1)
        
        
def CourbeKoch(n,cote):
    if n == 0:
        forward(cote)
    else:
        CourbeKoch(n-1,cote/3)
        left(60)
        CourbeKoch(n-1,cote/3)
        right(120)
        CourbeKoch(n-1,cote/3)
        left(60)
        CourbeKoch(n-1,cote/3) 
        

def neige(flocon, x, y):
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
            CourbeKoch(3,100)
            left(360/n)
        end_fill()
        neige(flocon-1, randint(-300, 300), randint(-300, 300))
            
        

# CIEL
up()
goto(-475, 400)
setheading(0)
down()
color('#27C3FA')
begin_fill()
rectangle(1, 950, 300)
end_fill()

# PLAGE
up()
goto(-475, -100)
setheading(0)
down()
color('#E5DB35')
begin_fill()
rectangle(1, 950, 300)
end_fill()

# MER
up()
goto(-475, 100)
setheading(0)
down()
color('#1165B0')
begin_fill()
rectangle(1, 950, 200)
end_fill()

# SOLEIL
up()
goto(0, 100)
setheading(0)
down()
color('#F0F770')
begin_fill()
circle(55)
end_fill()

# REFLET DU SOLEIL
up()
goto(-75, 95)
setheading(0)
down()
color('#E7E7E7')
pensize(5)
zigzag(10, 150, 95)
pensize(1)

speed(0)
# NUAGE
up()
goto(-300, 300)
setheading(0)
down()
color('#CBCBCB')
begin_fill()
nuage(4)
end_fill()

# LUNE
up()
goto(300, 350)
setheading(0)
down()
color('#FAF9DA')
begin_fill()
demi_cercle(1, "r")
right(90)
forward(115)
end_fill()
speed(5)


# DECORS


# PALMIER
setheading(0)
tron(5, 150, -275, -300)
forward(150/5)
speed(0)
feuille(3)

# SERVIETTE
up()
goto(100, -150)
setheading(0)
down()
serviette(5)
autre_serviette = input("Voulez-vous une deuxième serviettes ? O / N ")
if autre_serviette == "O":
    up()
    goto(215, -150)
    setheading(0)
    down()
    serviette(5)
    

# BONUS
print()
print("Ce paysage est actuellement une plage pendant la saison d'été.")
saison = input("Voulez-vous ajouter un effet de neige ? O / N ")
if saison == "O":
    nombre_flocon = int(input("Combien de flocon voulez-vous ? (0 = aléatoire entre 3 et 10) "))
    speed(0)
    x = randint(-300, 300)
    y = randint(-300, 300)
    if nombre_flocon == 0:
        flocon = randint(5, 50)
        neige(flocon, x, y)
    else:      
        neige(nombre_flocon, x, y)
    print()
    print("Votre paysage est enfin fini !")
elif saison == "N":
    print()
    print("Votre choix a bien été prit en compte le dessin est donc terminé !")
up()
goto(450, -400)
down()
color('#000000')
style = ('Courier', 20, 'bold')
write("Eliott", font=style, align='right')


exitonclick()
