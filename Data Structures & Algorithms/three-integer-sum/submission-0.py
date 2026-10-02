class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # iterate through each item
        # then maybe store in some kind of hash map e.g. dict
        # for each item calculate its complement (then store it as values)
        # use two pointer to find the values that make up for that complement (i.e. two integer sum 2 solution)
        # essentially answer is just the key, two integer sum answer (total 3 values)
        res = set()
        nums.sort()

        for i_num in range(len(nums)):
            i = i_num + 1
            j = len(nums) - 1
            # find two values in the array that sum to the negative of each value in the array to so that total sum is 0
            while i < j:
                # if too small, i++ to get larger value
                if nums[i] + nums[j] < -nums[i_num]:
                    i += 1
                # if too big, j-- to get a smaller value
                elif nums[i] + nums[j] > -nums[i_num]:
                    j -= 1
                else:
                    res.add((nums[i_num], nums[i], nums[j]))
                    i += 1
                    j -= 1

        return list(res)
                


[-4, -1, -1, 0, 1, 2, 3, 4]
        
        