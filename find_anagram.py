#https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import Counter
def find_all_anagram(s,p):
    def is_anagram(c1,c2):
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c1[c]!=c2[c]:
                return False
        return True
    result=[]
    len_p=len(p)
    c2=Counter(p)
    c1=Counter(s[:len_p])
    if is_anagram(c1,c2):
       result.append(0)
    for i in range(1,len(s)-len_p+1):
        c1[s[i-1]]-=1
        c1[s[i+len_p-1]]+=1
        if is_anagram(c1,c2):
            result.append(i)
    return result
print(find_all_anagram('abab','ab') )