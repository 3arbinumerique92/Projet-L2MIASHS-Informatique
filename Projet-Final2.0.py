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
        
    




def generate_random_map(m, proportion_wall):
    
    total = len(m) * len(m[0])
    n = int(proportion_wall * total)
    indices = [(i, j) for i in range(len(m)) for j in range(len(m[0]))]
    
    indices_walls =random.sample(indices, n)
    for i, j in indices_walls:
        m[i][j] = 1
        
    entrée=random.sample(indices, 1)
    while entrée in indices_walls:
        entrée=random.sample(indices, 1)
    
    sortie=random.sample(indices, 1)
    while sortie in indices_walls or sortie in entrée:
        sortie=random.sample(indices, 1)
    
    for k,l in entrée:
        m[k][l] = 2
        
    for p,q in sortie:
        m[p][q] = 3
        
    
    
    return m


size_map = (random.randint(5, 10),random.randint(5, 10))
proportion = 0.3
                                 
dico = {0:' ',1:'#',2:" ",3:"X"}
map = generate_random_map([[0 for i in range(size_map[1])] for j in range(size_map[0])],proportion)




       

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
objects=create_objects(random.randint(4, len(map)), map)

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
        
    
    
def delete_all_walls(m,pos):
    x,y=pos
    
    def var_y(i,y):
        if y>0 and y<(len(m[i])-1):
            for j in [y-1,y,y+1]:
                if m[i][j]=="#":
                    m[i][j]=0
                    
        if y==0:
            for j in [y,y+1]:
                if m[i][j]=="#":
                    m[i][j]=0
                    
        if y==(len(m[i])-1):
            for j in [y-1,y]:
                if m[i][j]=="#":
                    m[i][j]=0
    
    if x>0 and x<(len(m)-1):
        for i in [x-1,x,x+1]:
            var_y(i,y)
            
    if x==0:
        for i in [x,x+1]:
            var_y(i,y)
        
    if x==(len(m)-1) :
        for i in [x-1,x]:
            var_y(i,y)
            
    
#   2.3-Déplacement

#1)

def update_p(letter,p,m,objects):      #modification 3.1
        
        
    Haut_Bas={"z":-1, "s":1}
    Gauche_Droite={"q":-1, "d":1}
    
    if letter in Haut_Bas:
        p["x"]+=Haut_Bas[letter]
        if p["x"]<0 or p["x"]>=len(m) or m[p["x"]][p["y"]]=="#" or (len(objects)!=0 and m[p["x"]][p["y"]]=="X") :
            p["x"]-=Haut_Bas[letter]
        else:
            m[p["x"]-Haut_Bas[letter]][p["y"]]=0
            
    if letter in Gauche_Droite:
        p["y"]+=Gauche_Droite[letter]
        if p["y"]<0 or p["y"]>=len(m[0]) or m[p["x"]][p["y"]]=="#" or (len(objects)!=0 and m[p["x"]][p["y"]]=="X"):
            p["y"]-=Gauche_Droite[letter]
        else:
            m[p["x"]][p["y"]-Gauche_Droite[letter]]=0
        
    if letter== " ":
        delete_all_walls(m,(p["x"],p["y"]))
    
    
     
    return p


def create_new_level(p, m, objects, size_map, proportion_wall):
    m=generate_random_map([[0 for i in range(size_map[0])] for j in range(size_map[1])], proportion_wall)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==2:
                p["x"],p["y"]=i,j
    objects=create_objects(random.randint(4, len(m)),m)
    
    return m,p,objects
         
        
display_map_char_and_objects(map, dico, p, objects)    

# 2.4 Jouer à l'infini
while True:
    letter=stdscr.getkey()
    if letter=="e":
        break
    stdscr.erase()
    p=update_p(letter,p,map, objects)
    objects,p = update_objects(p, objects)
    if map[p["x"]][p["y"]]=="X" :
        stdscr.erase()
        map,p,objects=create_new_level(p, map, objects, size_map, proportion)
        
    display_map_char_and_objects(map, dico, p, objects)
    
    stdscr.refresh()
