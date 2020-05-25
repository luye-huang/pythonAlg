from typing import List


class Solution:
    @staticmethod
    def merge(a, b, parents, depth):
        a = Solution.getRoot(Solution, a, parents)
        b = Solution.getRoot(Solution, b, parents)
        if a != b:
            if depth[a] <= depth[b]:
                parents[a] = b
                depth[a] = depth[b] + 1
            else:
                parents[b] = a
                depth[b] = depth[a] + 1

    def isConnect(self, a, b, parents):
        return self.getRoot(a, parents) == self.getRoot(b, parents)

    def getRoot(self, a, parents):
        while a != parents[a]:
            a = parents[a]
        return a

    def equationsPossible(self, equations: List[str]) -> bool:
        disconnects = []
        parents = [*range(0, 26)]
        depth = [0] * 26
        for eq in equations:
            a, exp, b = ord(eq[0])-97, eq[1:3], ord(eq[-1])-97
            if exp == '==':
                Solution.merge(a, b, parents, depth)
            else:
                disconnects.append([a, b])
        for dic in disconnects:
            if self.isConnect(dic[0], dic[1], parents):
                return False
        return True


s = Solution()
print(s.equationsPossible(["a==b", "b==c", "d==e", "e==f", "d==a", "f!=a"]))
print(s.equationsPossible(["a==b","b!=c","c==a"]))
print(s.equationsPossible(["c==c","b==d","x!=z"]))
print(s.equationsPossible(["f==b","c==b","c==b","e!=f"]))
