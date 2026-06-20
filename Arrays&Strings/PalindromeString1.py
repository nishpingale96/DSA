class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = "".join(char.lower() for char in s if char.isalnum())
        left,right = 0, len(cs)-1
        while left<=right:
            if (cs[left] == cs[right]):
                left += 1
                right -= 1
            else:
                return False
        return True