from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        length = len(positions)
        heights = [x[1] for x in positions]
        ret = heights.copy()
        for i in range(1, length):
            up = positions[i]
            height = 0
            for j in range(i):
                down = positions[j]
                if not (up[0] + up[1] <= down[0] or down[0] + down[1] <= up[0]):
                    height = max(height, heights[j])
            heights[i] += height
            ret[i] = max(ret[i - 1], heights[i])
        return ret


print(Solution.fallingSquares(Solution, [[2, 1], [2, 9], [1, 8]]))
print(Solution.fallingSquares(Solution, [[1, 2], [2, 3], [6, 1]]))
