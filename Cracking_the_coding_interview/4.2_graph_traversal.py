'''
4.2
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
'''

'''
General graph search solutions:
1) BFS if all edge costs are the same
2) UCS if edges costs are not the same
3) DFS if optimaliti is not required
4) A* search (if coordinates are known, use euclidean distance as the heuristic)

For this problem, edge costs do not matter and optimality does not matter. So we can simply use BFS

'''

# def genericSearch(graph,start,goal,priorityFunction,heuristic=nullHeuristic)

# FIFO
def bfsSearch(graph,start,goal):
    frontier = [start]
    explored = set()
    while frontier != []:
        cur = frontier.pop(0)
        if graph.goalCheck(cur,goal):
            return True
        for node in graph.successors(start):
            if node not in explored:
                frontier.append(node)
    return False
        
    