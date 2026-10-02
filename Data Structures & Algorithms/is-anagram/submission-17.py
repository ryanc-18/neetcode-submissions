class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        dictt = defaultdict(int)
        for i in s:
            dictt[i] += 1
        for j in t:
            dictt[j] -= 1

        print(dictt)
        print(math.prod(dictt.values()))

        values = [abs(i) for i in list(dictt.values())]
        if sum(values) == 0:
            return True    
        else:
            return False

            

        