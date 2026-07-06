graph={
    "A":["B","C"],
    "B":["D"],
    "C":["D"],
    "D":[]
}
for i in graph:
    print(i,graph[i])