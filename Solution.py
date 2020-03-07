class Solution:
    def __init__(self, maze):
        self.maze = maze

    def find_start(self):
        pos = [0, 0]
        for i in range(len(self.maze[0])):
            if self.maze[0][i] == 1:
                pos = [0, i]
        return pos

    def find_end(self):
        pos = [0,0]
        print len(self.maze)
        for i in range(len(self.maze[0])):
           if 1 == self.maze[len(self.maze)-1][i]:
                pos =[len(self.maze)-1,i]
        return pos
    def neighbors(self, node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            temp = [node[0] + dir[0], node[1] + dir[1]]
            #makes sure that the point is in the maze
            if (temp[0] < len(self.maze) and temp[0] > -1) and (temp[1] < len( self.maze[0]) and temp[1] > -1):
                if self.maze[temp[0]][temp[1]] == 1:
                    result.append(temp)
        return result

    def display(self):
        for x in range(0, len(self.maze)):
            print(self.maze[x])
