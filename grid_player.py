M = int(input("Enter the dimension of the grid: "))
N = int(input("Enter the choice by the player: ")) 
if N < M:     print("No points gained.")
else:
    free_cells = (N ** 2) - (M ** 2) 
    print("Points gained:", free_cells) 
