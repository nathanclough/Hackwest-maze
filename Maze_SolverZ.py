from PIL import Image
from collections import deque
img = Image.open('small.png')
data = list(img.getdata())
WIDTH, HEIGHT = img.size
size = WIDTH * HEIGHT
data = [data[offset:offset+WIDTH] for offset in range(0, size, WIDTH)]

queue = []
checked = []
def breadthSearch(checked, graph, s):
    checked.append(s)
    queue.append(s)
    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        for i in graph[s]:
            if i not in checked:
                queue.append(i)
                checked.append(i)

def shortestBFS(start, end, graph):
    found = set()
    queue = [[start]]
    if start == end:
        return"Found connections"
    while queue:
        path = queue.pop(0)
        element = path[-1]
        if element not in found:
            for i in graph.get(element,[]):
                new_path = list(path)
                new_path.append(i)
                queue.append(new_path)
                if i == end:
                    return new_path
            found.add(element)
arr = {(0, 1): [(1, 1)],
       (1, 2): [(1, 3), (1, 1)],
       (1, 3): [(2, 3), (1, 2)],
       (2, 1): [(1, 1)],
       (2, 4): [(3, 4), (2, 3)],
       (2, 3): [(2, 4), (1, 3)],
       (1, 0): [(1, 1)],
       (3, 4): [(2, 4)],
       (1, 1): [(2, 1), (1, 2), (0, 1), (1, 0)]}
print(shortestBFS((0,1),(3,4),arr))
