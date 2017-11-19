#import random

def description():
    return """The idea is building something like MST but a chain.
I just implement Kruskal's algorithm with only difference
that it does not let node have degree more than two. Because visiting one city twice is forbidden.
When all nodes are added into path, just add last edge, so that it creates a circle.
    """


def tsp(data):
    # class A:
    #     @staticmethod
    #     def len(obj):
    #         if obj == None:
    #             return 0
    #         return len(obj)

    def inChain(vertex):
        for chain in chains:
            if vertex in chain:
                return chains.index(chain)

    edges = []
    for i in range(len(data)):
        for o in range(i + 1, len(data)):
            edges.append([i, o, ((data[o][0] - data[i][0]) ** 2 + (data[o][1] - data[i][1]) ** 2) ** 0.5])
    edges.sort(key=lambda x: x[2])
    #print(edges)
    edges_in_path = []
    directconnections = {}
    chains = []
    for edge in edges:
        if edge == edges[0]:
            continue
        for i in range(2):
            if edge[i] not in directconnections.keys():
                directconnections[edge[i]] = 0
        if directconnections[edge[0]] < 2 and directconnections[edge[1]] < 2:
            chain0 = inChain(edge[0])
            chain1 = inChain(edge[1])
            if chain0 == chain1 and chain0 is not None:
                continue
            if chain0 is not None and chain1 is not None:
                chains[chain0] += chains[chain1]
                chains.pop(chain1)
            elif chain0 is not None:
                chains[chain0].append(edge[1])
            elif chain1 is not None:
                chains[chain1].append(edge[0])
            else:
                chains.append([edge[0],edge[1]])
            edges_in_path.append(edge)
            for i in range(2):
                directconnections[edge[i]] += 1
    #print(summ)
    cs = []
    for c in directconnections:
        if directconnections[c]!= 2:
            cs.append(c)
    for edge in edges:
        if(edge[0] == cs[0] and edge[1] == cs[1]):
            edges_in_path.append(edge)
    length = 0
    for edge in edges_in_path:
        length += edge[2]
    path = [edges_in_path[0][0]]
    while edges_in_path:
        for edge in edges_in_path:
            if edge[0] == path[-1]:
                path.append(edge[1])
                edges_in_path.pop(edges_in_path.index(edge))
                break
            if edge[1] == path[-1]:
                path.append(edge[0])
                edges_in_path.pop(edges_in_path.index(edge))
                break
    sortero = path[-5:]+path[1:5]
   # def pathlen(path):

    return length,path