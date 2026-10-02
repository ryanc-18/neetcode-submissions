import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            new_list = nums[:i] + nums[i + 1:]
            res.append(math.prod(new_list))
        return res