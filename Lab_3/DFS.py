GRAPH={
    1:[2,3],
    2:[4,5],
    3:[6],
    4:None,
    5:[7,8],
    6:None,
    7:None,
    8:None
}

def DFS (start,target,GRAPH,layer):
    print "Source :",start," Target:",target
    stack=[start]
    visited=[]
    while len(stack)>0:
        x=stack.pop(0)
        if x== target:
            visited.append(x)
            return visited
        elif x not in visited:
            visited=visited+[x];
            if GRAPH[x] is not None:
                stack=GRAPH[x]+stack
    return  visited
print "DFS Path:",DFS(1,10,GRAPH,3)
print "="*80
print "DFS Path",DFS(1,3,GRAPH,2)

