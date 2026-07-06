stack=[]
stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)
for i in range(1,len(stack)+1):
    print(stack[-i])

if not stack:
    print("EMPTY")
else:
    print("Not EMPTY")