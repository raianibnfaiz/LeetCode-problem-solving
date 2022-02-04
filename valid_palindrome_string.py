#https://leetcode.com/problems/valid-palindrome/
def palindrome(s):
    s=[ch for ch in s if ch.isalnum()]
    s="".join(s)
    s=s.lower()
    left=0
    right=len(s)-1
    while(left<right):
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True
print(palindrome("A maN, a plan, a canal: Panama"))