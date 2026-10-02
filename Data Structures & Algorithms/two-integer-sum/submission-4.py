class Solution:     
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i in range(len(nums)):
            dictt[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            # check if difference to make target is in the hashmap
            # ... and ensure value found is different
            if diff in dictt.keys():
                if dictt[diff] != i:
                    return sorted([i, dictt[diff]])

