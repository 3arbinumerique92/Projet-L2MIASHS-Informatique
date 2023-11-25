 # Projet L2 MIASHS - Informatique: Mini Game     


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
              print(m[i][j], end=' ')
        print(" ")


def nul(size_map):
    
    M= [[0 for i in range(size_map[1])] for j in range(size_map[0])]
    return M



def Malea(m, proportion_wall):
    
    total = len(m) * len(m[0])
    n = int(proportion_wall * total)
    indices = [(i, j) for i in range(len(m)) for j in range(len(m[0]))]
    indices_hasard = random.sample(indices, n)
    for i, j in indices_hasard:
        m[i][j] = 1
    return m


size_map = (5, 5)
matrix = nul(size_map)
p = 0.3
                                 
dico = {0:' ',1: '#'}
map = Malea(matrix,p)




       

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
    print(p["score"])
 
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
    letter=input("Quel déplacement? ”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite):")  
    p=update_p(letter,p,map)
    objects,p = update_objects(p, objects)
    display_map_char_and_objects(map, dico, p, objects)
