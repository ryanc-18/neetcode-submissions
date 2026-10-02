class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        listt = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        # count frequency of each int
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        print(count)
        for i in count:
            listt[count[i]].append(i)

        for i in reversed(listt):
            for j in i:
                # return if we already retrieved k most frequent
                if len(res) == k:
                    return res
                res.append(j)

        return res


        