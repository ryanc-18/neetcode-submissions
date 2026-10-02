class Solution:
    def isPalindrome(self, s: str) -> bool:
        # combine sentence into one long string
        string = s.strip(" ")
        string_lower = string.lower()
        # remove non-alphanumeric characters
        cleaned = [c for c in string_lower if c.isalnum()]
        cleaned_lower_string = "".join(cleaned)
        string_length = len(cleaned_lower_string)
        print(cleaned_lower_string)
        for i in range(string_length):
            print("start: " + cleaned_lower_string[i] + " end: " + cleaned_lower_string[string_length - i - 1])
            if cleaned_lower_string[i] != cleaned_lower_string[string_length - i - 1]:
                return False
            if i == string_length - i - 1 or i > string_length - i - 1:
                return True
        return True
