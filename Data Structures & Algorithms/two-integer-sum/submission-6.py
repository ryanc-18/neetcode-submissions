class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        # store ints as keys and their indices as values
        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
                 

        