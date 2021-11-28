from turtle import* # import de toutes les fonctions de turtle
from random import randint # import de la fonction randint de random
from turtle_class import* # import de toutes les classes récursives ou non pour la création du dessin
bgcolor("black") # défini le fond en noir
setup(950, 800) # défini la fenêtre en px
title("Plage Récursive") # défini le titre de la fenêtre
speed(10) # défini la vitesse la plus rapide
shape('turtle') # défini le curseur en Tortue

# Appel de toutes les classes
g = Global()
m = Mer()
c = Ciel()
p = Palmier()
pl = Plage()
n = Neige()

# CIEL
up()
goto(-475, 400)
setheading(0)
down()
color('#27C3FA')
begin_fill()
g.rectangle(1, 950, 300)
end_fill()

# PLAGE
up()
goto(-475, -100)
setheading(0)
down()
color('#E5DB35')
begin_fill()
g.rectangle(1, 950, 300)
end_fill()

# MER
up()
goto(-475, 100)
setheading(0)
down()
color('#1165B0')
begin_fill()
g.rectangle(1, 950, 200)
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
m.zigzag(10, 150, 95)
pensize(1)

speed(0)
# NUAGE
up()
goto(-300, 300)
setheading(0)
down()
color('#CBCBCB')
begin_fill()
c.nuage(4)
end_fill()

# LUNE
up()
goto(300, 350)
setheading(0)
down()
color('#FAF9DA')
begin_fill()
g.demi_cercle(1, "r")
right(90)
forward(115)
end_fill()
speed(5)

# PALMIER
setheading(0)
p.tron(5, 150, -275, -300)
forward(150/5)
speed(0)
p.feuille(3)

# SERVIETTE
up()
goto(100, -150)
setheading(0)
down()
pl.serviette(5)
autre_serviette = input("Voulez-vous une deuxième serviettes ? O / N ")
if autre_serviette == "O":
    up()
    goto(215, -150)
    setheading(0)
    down()
    pl.serviette(5)
    

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
        n.neige(flocon, x, y)
    else:      
        n.neige(nombre_flocon, x, y)
    print()
    print("Votre paysage est enfin fini !")
elif saison == "N":
    print()
    print("Votre choix a bien été prit en compte le dessin est donc terminé !")
    

# SIGNATURE
up()
goto(450, -400)
down()
color('#000000')
style = ('Courier', 20, 'bold')
write("Eliott", font=style, align='right')


exitonclick()
