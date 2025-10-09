import json

data = json.loads(input())
graph = {}
classes = set()

for item in data:
    name = item["name"]
    parents = item["parents"]
    classes.add(name)
    for p in parents:
        graph.setdefault(p, []).append(name)
    graph.setdefault(name, [])

def get_descendants(cls, visited=None):
    if visited is None:
        visited = set()
    for child in graph.get(cls, []):
        if child not in visited:
            visited.add(child)
            get_descendants(child, visited)
    return visited
  
result = {}
for cls in classes:
    descendants = get_descendants(cls)
    result[cls] = len(descendants) + 1

for name in sorted(result):
    print(f"{name} : {result[name]}")
