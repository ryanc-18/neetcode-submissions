class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        # calculate prefix of each item
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]

        print(res)

        postfix = 1
        # calculate postfix
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]


        return res



        