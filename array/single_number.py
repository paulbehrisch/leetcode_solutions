from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for k in counts:
            if counts[k] == 1:
                return k

x = Solution()
print(x.singleNumber(nums=[2,2,1]))
print(x.singleNumber(nums=[4,1,2,1,2]))
