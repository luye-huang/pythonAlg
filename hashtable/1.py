from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, v in enumerate(nums):
            if v in dict:
                return [dict[v], i]
            dict[target-v] = i
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
