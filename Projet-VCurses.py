  # Projet L2 MIASHS - Informatique: Mini Game     

import curses

stdscr = curses.initscr()
curses.noecho()

#        2-AFFICHAGE DE BASE

#   2.1-Carte
import random


def display_map (m, d):
    for i in range(len (m)) :
        for j in range(len (m[i])):
            if m[i][j] in d:
                m[i][j]=d[m[i][j]]
                
    for i in range(len(map)):
        for j in range(len(map[i])):
              stdscr.addstr(i, j, str(m[i][j]))
        
    
                                 
dico = {0:' ',1: '#'}
map = [[0,0,0, 1,1], [0,0,0,0,1,],[1,1,0,0,0,], [0,0,0,0,0]]




       

#   2.2-Personnage
       
#1)
def create_perso (n,m,score) :
    return {"char":"o", "x":n, "y":m, "score":score}
    
p=create_perso (0,0,0)
#print (d)

#3)
def display_map_and_char (m, d,p):
    m[p["x"]][p["y"]]=p["char"]
    display_map(map, dico)

def create_objects(nb_objects, m):
    positions = set()
    
    while len(positions) < nb_objects:
        x = random.randint(0, len(m) - 1)
        y = random.randint(0, len(m[0]) - 1)

        if m[x][y] == 0:
            positions.add((x, y))

    return positions
objects=create_objects(2, map)

def display_map_char_and_objects(m, d, p, objects):
    for duo in objects:
        m[duo[0]][duo[1]]="."
    display_map_and_char (map, dico,p)
    stdscr.addstr(len(m), 0, str(p["score"]))
 
#3.5 Ramasser auto les objets
def update_objects(p, objects):
    if (p["x"],p["y"]) in objects:
        objects.remove((p["x"],p["y"]))
        p["score"]+=1
    return objects,p
        
    
    
#4)


#   2.3-Déplacement

#1)

def update_p(letter,p,m):              #modification 3.1
    Haut_Bas={"z":-1, "s":1}
    Gauche_Droite={"q":-1, "d":1}
    
    if letter in Haut_Bas:
        p["x"]+=Haut_Bas[letter]
        if p["x"]<0 or p["x"]>=len(m) or m[p["x"]][p["y"]]=="#":
            p["x"]-=Haut_Bas[letter]
        else:
            m[p["x"]-Haut_Bas[letter]][p["y"]]=0
            
    if letter in Gauche_Droite:
        p["y"]+=Gauche_Droite[letter]
        if p["y"]<0 or p["y"]>=len(m[0]) or m[p["x"]][p["y"]]=="#":
            p["y"]-=Gauche_Droite[letter]
        else:
            m[p["x"]][p["y"]-Gauche_Droite[letter]]=0
            
    return p

display_map_char_and_objects(map, dico, p, objects)    

# 2.4 Jouer à l'infini
while True:
    letter=stdscr.getkey()
    stdscr.erase()
    p=update_p(letter,p,map)
    objects,p = update_objects(p, objects)
    display_map_char_and_objects(map, dico, p, objects)
    if len(objects)==0:
        stdscr.erase()
        stdscr.addstr(12, 25, "Vous avez gagné!")
        stdscr.refresh()
        break
    stdscr.refresh()
    
