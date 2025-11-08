from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
      node = frontier.pop() #Visits and removes most recent node
      for neighbor in graph[node]: #Checks all nodes adjacent to current node
          if neighbor not in result: # Only add those not in result to frontier, prevents redundancy
                result.add(neighbor)
                frontier.add(neighbor)
       
    return result





def connected(graph):
    start_node = min(graph)  #Picks smallest node to start, but any node can be picked since we are working with undirected graph
    reachable_nodes = reachable(graph, start_node)
    
    return len(reachable_nodes) == len(graph) #Returns true if same length (reachable set same as graph implies all nodes reached), false otherwise



def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    unvisited = set(graph.keys()) #Initializes set with all nodes
    count = 0
    
    while unvisited:
        node = unvisited.pop()           # Pick an arbitrary unvisited node
        reachable_nodes = reachable(graph, node)
        unvisited -= reachable_nodes     # Remove all nodes in this component to avoid redundant calls
        count += 1 #Iterate num components
    
    return count
    

