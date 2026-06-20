class Solution:
    def validPalindrome(self, s: str) -> bool:
        mid = len(s)//2
        new_s = s[:mid] + s[mid + 1:]
        left, right = 0,len(new_s)-1
        while left<=right:
            if (new_s[left]==new_s[right]):
                left +=1
                right -=1
            else:
                return False    
        return True
