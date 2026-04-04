class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ""
        for letter in s:
            if letter.isalpha() == True or letter.isnumeric() == True:
                string += letter
        reverse = string[::-1]
        if string == reverse:
            return True
        return False