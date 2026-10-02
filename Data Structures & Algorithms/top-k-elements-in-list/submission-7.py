class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict to store freq count
        # create list where index represents freq count


        freq = {}
        # create a list of lists of size len(nums)
        listt = [[] for i in range(len(nums) + 1)]
        res = []
        # count freq of each num
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        # store num in corresponding count index
        for key in freq:
            print(str(key) + " " + str(freq[key]))
            listt[freq[key]].append(key)

        for i in listt[::-1]:
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res
        
        return []


        


        