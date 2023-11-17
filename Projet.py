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
       
       
       
def create_perso (n,m) :
       return {"char":"o", "x":n, "y":m}
    
p=create_perso (0,0)
#print (d)


def display_map_and_char (m, d,p):
    m=display_map (m, d)
    m[p["x"]][p["y"]]=p["char"]
    return m

for i in range(len(map)):
    for j in range(len(map[i])):
        print(display_map_and_char(map, dico, p)[i][j], end=' ')
    print(" ")    
