class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors


def build_graph(adjList):
    """
    adjList[i] 的结果是 val 属性为 i+1 的图的相邻节点的 val 值结果
    """
    ls_Node = [Node(val+1, []) for val in range(len(adjList))]
    for idx, ls_adj in enumerate(adjList):
        ls_Node[idx].neighbors = [ls_Node[j-1] for j in ls_adj]

    return ls_Node[0]


def showNode(node, ls_adj=None):
    visited = []
    while node:
        if node.val not in visited:
            ls_adj.append([j.val for j in node.neighbors])
            visited.append(node.val)
            if node.neighbors[0].val not in visited:
                node = node.neighbors[0]
            elif node.neighbors[1].val not in visited:
                node = node.neighbors[1]
            else:
                node = None
    print(ls_adj)


if __name__ == "__main__":
    ls_adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    res = build_graph(ls_adj)
    showNode(res, [])
    print(res.val, " === ", [node.val for node in res.neighbors])


