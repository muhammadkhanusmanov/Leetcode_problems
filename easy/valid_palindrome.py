class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                new_s+=s[i]
 
        right, left = 0, len(new_s)-1
        
        if left==-1:
            return True
        new_s = new_s.lower()
        while right<left:
            if not new_s[right] == new_s[left]:
                return False
            left-=1
            right+=1
        return True
            