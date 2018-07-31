#riadnwu@gmail.com
#06

graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}


def dfs(graph, node, goal, limit, visited=[]):
    #  else:
    #     print("Not found ",node, goal)
    if limit == 0:
        return
    if node not in visited:
        visited.append(node)
        # if node == goal:
        #  print("Goal is reachable ")
        #   return
        for i in graph[node]:
            if node == goal:
                return
            dfs(graph, i, goal, limit - 1, visited)

    return visited

# Gettibg inputs
goal = raw_input("Enter Goal: ")
#getting limit
limit = int(input("Enter Limit: "))

# printing the visited sequence
visited_seq = dfs(graph, 'A', goal, limit)
print(visited_seq)

# print if reachacable or not
if goal in visited_seq:
    print("Reachable")
else:
    print("Not Reachable")