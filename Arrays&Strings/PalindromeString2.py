class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Mismatch encountered!
                # Option 1: Skip the left character
                skip_left = s[left + 1 : right + 1]
                # Option 2: Skip the right character
                skip_right = s[left : right]
                
                # If either substring is a perfect palindrome, we are golden
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
                
        return True
