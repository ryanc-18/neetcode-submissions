class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt = {}
        for i in s:
            if i in dictt.keys():
                dictt[i] += 1
            else:
                dictt[i] = 1

        for j in t:
            try:
                dictt[j] -= 1
            except:
                return False

        print(dictt.values())

        for i in dictt.values():
            if i != 0:
                return False
        
        return True
                

        
        
        