# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 07:35:37 2017

@author: Tanvir
"""

def dfs(g, v, goal, limit=-1):

    SENTINEL = object()    
    visitedStack = [v]
    path = ""

    while visitedStack:
        currentVertex = visitedStack.pop()    

        if g.getVertex(currentVertex) != None:
            if g.getVertex(currentVertex).visited == False:
                path += currentVertex + ' -> '

                g.getVertex(currentVertex).hasBeenVisited()

                if currentVertex == goal: 
                    return path[:-3]

                elif currentVertex == SENTINEL:
                    limit += 1

                elif limit != 0:
                    limit -= 1
                    visitedStack.append(SENTINEL)
                    visitedStack.extend(g.getVertex(currentVertex).getConnections()) 

    return "Depth limit was reached"

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

dfs(GRAPH,1,4,2)