class Solution:
    def __init__(self, maze):
        self.maze = maze

    def display(self):
        #print(len(self.maze));
        for x in range(0,len(self.maze)):
            print(self.maze[x])

