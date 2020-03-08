from PIL import Image
from Solution import Solution

img = Image.open('small.png')
data = list(img.getdata())
WIDTH, HEIGHT = img.size
size = WIDTH * HEIGHT
data = [data[offset:offset+WIDTH] for offset in range(0, size, WIDTH)]
s = Solution(data)
queue = []
checked = []

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

s.get_nodes()
arr = s.get_dict()
start = s.find_start()
print start
end = s.find_end()
print end
print arr
'''{(0, 1): [(1, 1)],
       (1, 2): [(1, 3), (1, 1)],
       (1, 3): [(2, 3), (1, 2)],
       (2, 1): [(1, 1)],
       (2, 4): [(3, 4), (2, 3)],
       (2, 3): [(2, 4), (1, 3)],
       (1, 0): [(1, 1)],
       (3, 4): [(2, 4)],
       (1, 1): [(2, 1), (1, 2), (0, 1), (1, 0)]}'''
print(shortestBFS(start,end,arr))
