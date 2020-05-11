from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            while nums.count(num) > 1:
                nums.remove(num)
        return nums

x = Solution()
print(x.removeDuplicates([1,1,1,2,2,3]))
