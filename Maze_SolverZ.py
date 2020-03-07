from PIL import Image
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
    found = []
    queue = [[start]]
    if start == end:
        return"Found connections"
    while queue:
        path = queue.pop(0)
        element = path[-1]
        if element not in found:
            neighbor = graph[element]
            for i in neighbor:
                new_path = list(path)
                new_path.append(i)
                queue.append(new_path)
                if i == end:
                    return new_path
            found.append(element)
arr = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
print(shortestBFS('A','F',arr))