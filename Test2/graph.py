graph={
    "A":["B","C"],
    "B":["D"],
    "C":["D"],
    "D":[]
}
visited=set()
def dfs(node):
    if node in visited:
        return
    print(node)
    visited.add(node)
    for i in graph[node]:
        dfs(i)

dfs("A")
print("\n")
vist=set()
queue=[]
queue.append("A")
while queue:
    node=queue.pop(0)
    if node not in vist:
        print(node)
        vist.add(node)
        for i in graph[node]:
            queue.append(i)
            
for i in graph:
    print(i,graph[i])