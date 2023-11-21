 # Projet L2 MIASHS - Informatique: Mini Game     


#        2-AFFICHAGE DE BASE

#   2.1-Carte
import random

def display_map (m, d):
    for i in range(len (m)) :
        for j in range(len (m[i])):
            if m[i][j] in d:
                m[i][j]=d[m[i][j]]
    return m
                                 
dico = {0:' ',1: '#'}
map = [[0,0,0, 1,1], [0,0,0,0,1,],[1,1,0,0,0,], [0,0,0,0,0]]
       
#for i in range(len (map)):
    #for j in range(len (map[i])):
        #print(display_map (map, dico)[i][j], end=' ')
    #print(" ")   
       

#   2.2-Personnage
       
#1)
def create_perso (n,m,score) :
    return {"char":"o", "x":n, "y":m, "score":score}
    
p=create_perso (0,0,0)
#print (d)

#3)
def display_map_and_char (m, d,p):
    m=display_map (m, d)
    m[p["x"]][p["y"]]=p["char"]
    return m

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
    m=display_map_and_char (m, d,p)
    for duo in objects:
        m[duo[0]][duo[1]]="."
    return m
 
#3.5 Ramasser auto les objets
def update_objects(p, objects):
    if (p["x"],p["y"]) in objects:
        objects.remove((p["x"],p["y"]))
        p["score"]+=1
    return objects,p
        
    
    
#4)
for i in range(len(map)):
    for j in range(len(map[i])):
        print(display_map_char_and_objects(map, dico, p,objects)[i][j], end=' ')
    print(" ")
    

#   2.3-Déplacement

#1)

def update_p(letter,p,m):              #modification 3.1
    Haut_Bas={"z":-1, "s":1}
    Gauche_Droite={"q":-1, "d":1}
    
    if letter in Haut_Bas:
        p["x"]+=Haut_Bas[letter]
        if p["x"]<0 or p["x"]>=len(m) or m[p["x"]][p["y"]]=="#":
            p["x"]-=Haut_Bas[letter]
        
    if letter in Gauche_Droite:
        p["y"]+=Gauche_Droite[letter]
        if p["y"]<0 or p["y"]>=len(m[0]) or m[p["x"]][p["y"]]=="#":
            p["y"]-=Gauche_Droite[letter]
            
    return p



# 2.4 Jouer à l'infini
while True:
    letter=input("Quel déplacement? ”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite):")  
    p=update_p(letter,p,map)
    map = [[0,0,0, 1,1], [0,0,0,0,1,],[1,1,0,0,0,], [0,0,0,0,0]]
    map=display_map(map, dico)
    objects,p = update_objects(p, objects)
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(display_map_char_and_objects(map, dico, p, objects)[i][j], end=' ')
        print(" ")
    print(p["score"])
