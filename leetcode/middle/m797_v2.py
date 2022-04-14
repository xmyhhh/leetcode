"""
m567.py
"""
from typing import List
import copy


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph) - 1
        res = list()
        path = list()

        def traverse(node):
            path.append(node)
            if node == n:
                res.append(copy.copy(path))
                path.pop()
                return
            for i in graph[node]:
                traverse(i)

            path.pop()

        traverse(0)
        return res

    def run(self):
        print("run m797_v2")
        print(self.allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
