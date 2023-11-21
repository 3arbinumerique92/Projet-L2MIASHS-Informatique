 # Projet L2 MIASHS - Informatique: Mini Game     


#        2-AFFICHAGE DE BASE

#   2.1-Carte


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
def create_perso (n,m) :
    return {"char":"o", "x":n, "y":m}
    
p=create_perso (0,0)
#print (d)

#3)
def display_map_and_char (m, d,p):
    m=display_map (m, d)
    m[p["x"]][p["y"]]=p["char"]
    return m


#4)
for i in range(len(map)):
    for j in range(len(map[i])):
        print(display_map_and_char(map, dico, p)[i][j], end=' ')
    print(" ")
    

#   2.3-Déplacement

#1)

def update_p(letter,p):
    Haut_Bas={"z":-1, "s":1}
    Gauche_Droite={"q":-1, "d":1}
    
    if letter in Haut_Bas:
        p["x"]+=Haut_Bas[letter]
    if letter in Gauche_Droite:
        p["y"]+=Gauche_Droite[letter]
        
    return p


# 2.4 Jouer à l'infini
while True:
    letter=input("Quel déplacement? ”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite):")  
    p=update_p(letter,p)
    map = [[0,0,0, 1,1], [0,0,0,0,1,],[1,1,0,0,0,], [0,0,0,0,0]]                            #ajouter une fonction qui remplace ce truc bien loooooong
    map=display_map(map, dico)
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(display_map_and_char(map, dico, p)[i][j], end=' ')
        print(" ")


