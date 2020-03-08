from Solution import Solution
#5x5 test maze
rows, cols = (4, 5)
maze = [[0 for i in range(cols)] for j in range(rows)]
maze[0][1] = 1
maze[1][0] = 1
maze[1][1] = 1
maze[1][2] = 1
maze[1][3] = 1
maze[2][1] = 1
maze[2][3] = 1
maze[2][4] = 1
maze[3][4] = 1
sol = Solution(maze)
print(sol.get_nodes())
sol.display()










