from PIL import Image
import Joey
import file_Picker
from Solution import Solution
import timeit
file = file_Picker.opener()
img = Image.open(file)
data = list(img.getdata())
WIDTH, HEIGHT = img.size
size = WIDTH * HEIGHT
data = [data[offset:offset+WIDTH] for offset in range(0, size, WIDTH)]
s = Solution(data)
queue = []
checked = []
Start = timeit.default_timer()
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
a = shortestBFS(start,end,arr)
Final = timeit.default_timer()
print('Time: ', Final - Start)
Joey.DrawMaze(file,a)
