def solveMaze(maze, endp):
    sol = []
    for i in range(len(maze)):
        sol.append([0]*len(maze[i]))
    while (sol[endp[0]][endp[1]] != 1):
          

maze = [[1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0]
]

endp = [4,4]
a = solveMaze(maze, endp)
if a is not None:
    for i in a:
        print(i)
