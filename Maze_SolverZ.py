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
end = s.find_end()
print(shortestBFS(start,end,arr))
