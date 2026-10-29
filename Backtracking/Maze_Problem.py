def solveMaze(maze):
    sol = []
    for i in range(len(maze)):
        sol.append([0]*len(maze[i]))

    if(solveMazeUtil(maze,0,0,sol) == False):
        print("SOlution doesn't exist")
        return False
    printSolution(sol)
    return True

def solveMazeUtil(maze, x,y,sol):
    #if (x, y is goal) return true/
    if (x == N-2 and y == M-1 and maze[x][y] == 1):
        sol[x][y] = 1
        return True
    
    #Check if maze[x][y] is valid
    if(isSafe(maze, x,y) == True):
        #Check if the current block is already part of solution path.
        if (sol[x][y] == 1):
            return False
        #mark x, y as part of solution path
        sol[x][y] = 1
        
        #Move in direction
        if (solveMazeUtil(maze, x+1, y, sol) == True):
            return True
        
        #if moving in x direction doesn't give solution then Move in y direction
        if (solveMazeUtil(maze, x,y+1, sol) == True):
            return True
        
        #if none of the above movement work then BACKTRACK: unmark x, y as part of solution path
        sol[x][y] = 0
        return False
    return False

def isSafe(maze, x, y):
    #if (x, y outside maze) return False
    if (x >= 0 and x <N and y>=0 and y<M and maze[x][y] == 1):
        return True
    
    return False

def printSolution(sol):
    for i in range(N):
        for j in range(M):
            print(sol[i][j], end=" ")
        print()


N = 6  #Baris ke
M = 5  #Kolom Ke
maze = [[1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0]
]

solveMaze(maze)