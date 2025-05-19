co=[[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]]


def show_tab():
    print(co[0])
    print(co[1])
    print(co[2])
    print(co[3])
    print(co[4])
    print(co[5])

show_tab()

player=1
game=0

def player_round(player):
    if player == 1:
        player = 2
        print("c'est ton tour, Joueur 1!")
    elif player == 2:
        player = 1
        print("c'est ton tour, Joueur 2!")
    return player

def verification(co):
    for y in range (3):
         for x in range (4):
              if co[y][x] == co[y][x+1] == co[y][x+2] == co[y][x+3] and co[y][x] != 0:
                  print("gg")
    for y in range (3):
         for x in range (7):
              if co[y][x] == co[y+1][x] == co[y+2][x] == co[y+3][x] and co[y][x] != 0:
                  print("gg")
    for y in range (6):
         for x in range (4):
              if co[y][x] == co[y-1][x+1] == co[y-2][x+2] == co[y-3][x+3] and co[y][x] != 0:
                  print("gg")
    for y in range (3):
         for x in range (4):
              if co[y][x] == co[y+1][x+1] == co[y+2][x+2] == co[y+3][x+3] and co[y][x] != 0:
                  print("gg")

y=0
done = False

while game != 1:
    if player == 1:
        
        print("c'est ton tour, Joueur 1!")
        x = int(input("quelle case?"))
        while y < 5 and done != True:
                if co[y+1][x] != 0:
                    co[y][x]=player
                    done=True
                    y=0
                else:
                    y+=1
        if y==5 and done == False:
            co[y][x]=player
            y=0
        player = 2
        done=False
        show_tab()
        
    verification(co)
    y=0
    x=0
            
    if player == 2:
        
        print("c'est ton tour, Joueur 2!")
        x = int(input("quelle case?"))
        while y < 5 and done != True:
                if co[y+1][x] != 0:
                    co[y][x]=player
                    done=True
                    y=0
                else:
                    y+=1
        if y==5 and done == False:
            co[y][x]=player
            y=0
        player = 1
        done=False
        show_tab()
        
    verification(co)

    y=0
    x=0
    
        
    
    