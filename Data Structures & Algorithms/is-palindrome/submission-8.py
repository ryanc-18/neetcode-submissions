class Solution:
    def isPalindrome(self, s: str ) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            print(f"start={start}, end={end}")
            while start < end and not self.isAlpha(s[start]):
                start += 1
            while start < end and not self.isAlpha(s[end]):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False 
            start += 1
            end -= 1
        return True


    def isAlpha(self, char):
        asc = ord(char)
        if (48 <= asc < 58 
           or 65 <= asc < 91 
           or 97 <= asc < 123):
            return True
        else: 
            return False