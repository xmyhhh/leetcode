import queue
import networkx as nx

import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def TreeNodeCreate(val=0, left=None, right=None):
    if val is not None:
        return TreeNode(val,left,right)
    else:
        return None
def treeBuild(treeList):
    nodeQueue = queue.Queue()
    i = 0
    alen = len(treeList)
    if treeList:
        root = TreeNodeCreate(treeList[0])
        nodeQueue.put(root)
        i += 1
    while i < alen:
        aNode = nodeQueue.get()
        node1 = TreeNodeCreate(treeList[i])
        nodeQueue.put(node1)
        aNode.left = node1
        if i + 1 < alen:
            node2 = TreeNodeCreate(treeList[i + 1])
            nodeQueue.put(node2)
            aNode.right = node2
        i += 2
    return root


def treeDraw(node):  # 以某个节点为根画图
    def create_graph(G, node, pos={}, x=0, y=0, layer=1):
        pos[node.val] = (x, y)
        if node.left and node.left.val:
            G.add_edge(node.val, node.left.val)
            l_x, l_y = x - 1 / 2 ** layer, y - 1
            l_layer = layer + 1
            create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
        if node.right and node.right.val:
            G.add_edge(node.val, node.right.val)
            r_x, r_y = x + 1 / 2 ** layer, y - 1
            r_layer = layer + 1
            create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
        return (G, pos)

    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()


# res = treeBuild(treeList=[5,4,6,None,None,3,7])
# treeDraw(res)
