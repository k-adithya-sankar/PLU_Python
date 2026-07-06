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