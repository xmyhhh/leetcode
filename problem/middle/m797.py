"""
m567.py
"""
from typing import List


class Solution:
    def printWithTab(self, val):
        print("    " * self.nTab + str(val))

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.nTab = 0
        self.graph = graph
        self.n = len(graph) - 1
        self.res = list()
        self.path = list()
        self.traverse(0)
        return self.res

    def traverse(self, node):
        self.nTab += 1
        self.path.append(node)

        self.printWithTab("go to node " + str(node) + "  currnet path " + str(self.path))
        import copy
        if node == self.n:
            self.res.append(copy.copy(self.path))

            self.printWithTab("find path" + str(self.path))

            self.path.pop()
            self.printWithTab("return" + "  currnet path " + str(self.path))
            self.nTab -= 1
            return
        for i in self.graph[node]:
            self.traverse(i)
        self.path.pop()

        self.printWithTab("return" + "  currnet path " + str(self.path))
        self.nTab -= 1

    def run(self):
        print("run m797")
        print(self.allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
