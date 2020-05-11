from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            last_number = nums.pop(-1)
            nums.insert(0, last_number)
        return nums

x = Solution()
print(x.rotate(nums=[-1,-100,3,99],k=2))
