class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 1
        prev = 0
        numset = set(nums)
        for i in numset:
            if (i - 1) in numset:
                continue

            currlen = 1
            j = 1
            while i + j in numset:
                print(i)
                currlen += 1
                j += 1
            
            longest = max(longest, currlen)
        
        return longest
            



             
        