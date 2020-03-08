
class Solution:
    def __init__(self, maze):
        self.maze = maze
        self.nodes = {}
    def find_start(self):
        pos = [0, 0]
        for i in range(len(self.maze[0])):
            if self.maze[0][i] == 1:
                pos = (0, i)
        return pos

    def find_end(self):
        pos = [0,0]
        for i in range(len(self.maze[0])):
           if 1 == self.maze[len(self.maze)-1][i]:
                pos =(len(self.maze)-1,i)
        return pos
    def neighbors(self, node):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        result = []
        for dir in dirs:
            temp = (node[0] + dir[0], node[1] + dir[1])
            #makes sure that the point is in the maze
            if (temp[0] < len(self.maze) and temp[0] > -1) and (temp[1] < len( self.maze[0]) and temp[1] > -1):
                if self.maze[temp[0]][temp[1]] == 1:
                    result.append(temp)
        return result
    def get_nodes(self):
        r = 0
        c = 0
        for row in self.maze:
            for col in row:
                if self.maze[r][c] == 1:
                    self.nodes[(r,c)] = self.neighbors((r,c))
                c = c+1
            c=0
            r = r + 1
    def display(self):
        print(self.nodes)
    def get_dict (self):
        return self.nodes