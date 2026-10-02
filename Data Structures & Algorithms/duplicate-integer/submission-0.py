class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Dictionary to store numbers that appear in the list and their count
        mydict = {}

        # Count when numbers appear in the list
        for i in range(0, len(nums)):
            if nums[i] in mydict:
                mydict[nums[i]] += 1
            else:
                mydict[nums[i]] = 1

        print(mydict)

        # Total count is less number of distinct numbers
        if sum(mydict.values()) > len(set(nums)):
            return True
        else:
            return False

