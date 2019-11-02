from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        ret = []
        h, w = len(grid), len(grid[0])
        if h == 0 or len(hits) == 0:
            return ret

        def isValid(y, x, visited) -> bool:
            return y >= 0 and x >= 0 and y < h and x < w and grid[y][x] == 1 and (y, x) not in visited

        def walk(co: tuple, visited) -> []:
            [y, x] = co
            bricks = []
            if isValid(y, x + 1, visited):
                visited[(y, x + 1)] = True
                bricks.append((y, x + 1))
            if isValid(y, x - 1, visited):
                visited[(y, x - 1)] = True
                bricks.append((y, x - 1))
            if isValid(y + 1, x, visited):
                visited[(y + 1, x)] = True
                bricks.append((y + 1, x))
            return bricks

        for hit in hits:
            hit = tuple(hit)
            visited = {}
            queue = walk(hit, {})
            grid[hit[0]][hit[1]] = 0
            possibleAll = set()
            for dir in queue:
                if dir in visited:
                    continue
                safe = False
                processing = [dir]
                possible = set()
                possible.add(dir)
                # 初代终止条件：1在第一行 2 上面一个存在且与hit平级以上
                if not dir[0] or dir[0] <= hit[0] and grid[dir[0] - 1][dir[1]] == 1:
                    safe = True
                    possible.discard(dir)
                while len(processing):
                    cur = processing.pop()
                    adj = walk(cur, visited)
                    for brick in adj:
                        # 终止条件：1在第一行 2 上面一个存在且(与hit平级以上或已经在第二行）
                        if not brick[0] or (brick[0] <= hit[0] or brick[0] == 1) and grid[brick[0] - 1][brick[1]] == 1:
                            safe = True
                        else:
                            possible.add(brick)
                        processing.insert(0, brick)
                if not safe:
                    possibleAll = possibleAll.union(possible)
            ret.append(len(possibleAll))
            for brick in possibleAll:
                grid[brick[0]][brick[1]] = 0
        return ret


print(Solution.hitBricks(Solution, [[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]]), '0,3,0')
print(Solution.hitBricks(Solution, [[1, 1, 0, 1, 0],
                                    [1, 1, 0, 1, 1],
                                    [0, 0, 0, 1, 1],
                                    [0, 0, 0, 1, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]]
                         , [[5, 1], [1, 3]]), '0,4')

print(Solution.hitBricks(Solution, [[0, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 0],
                                    [1, 1, 1, 1, 0],
                                    [0, 0, 1, 1, 0], [0, 0, 1, 0, 0],
                                    [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                         [[6, 0], [1, 0], [4, 3], [1, 2], [7, 1], [6, 3], [5, 2], [5, 1], [2, 4], [4, 4], [7, 3]]),
      '全为0')
print(Solution.hitBricks(Solution, [[1, 1, 1], [0, 1, 0], [0, 0, 0]], [[0, 2], [2, 0], [0, 1], [1, 2]]), '0,0,1,0')
print(Solution.hitBricks(Solution, [[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]), '2')
print(Solution.hitBricks(Solution, [[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]), '0,0')
print(Solution.hitBricks(Solution, [[1], [1], [1], [1], [1]], [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]), '1,0,1,0,0')
