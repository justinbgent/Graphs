from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    parentIndex = 0
    childIndex = 1
    #noParent = -1

    graphChildToParent = Graph()

    for relationship in ancestors:
        graphChildToParent.add_vertex(relationship[parentIndex])
        graphChildToParent.add_vertex(relationship[childIndex])

    for relationship in ancestors:
        graphChildToParent.add_edge(relationship[childIndex], relationship[parentIndex])

    return graphChildToParent.bftFindFarthest(starting_node)

    #earliest = graphChildToParent.bftFindFarthest(starting_node)

    #if earliest == starting_node:
    #    return noParent
    #else:
    #    return earliest