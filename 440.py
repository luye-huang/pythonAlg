import math


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:



        # print(len(str(n)))
        return ret

    def helper(num, rg):
        length = len(str(num))
        if length == 1:
            return {'ch': str(num), 'number': 0}
        return {'ch': str(rg[math.floor(num / math.pow(10, length - 1)) - 1]), 'number': num % math.pow(10, length - 1)}
    # print(Solution.findKthNumber(Solution, 13, 2))


print(Solution.helper(24, range(1, 9)))

print(Solution.helper(2, range(1, 9)))
# print(9 / 4)
# print(range(0, 9)[0])
