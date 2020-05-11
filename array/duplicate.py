from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        #print(vals)
        for k in counts:
            if counts[k] > 1:
                return True
        return False

x = Solution()
print(x.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))
print(x.containsDuplicate(nums=[1,2,3,4]))
