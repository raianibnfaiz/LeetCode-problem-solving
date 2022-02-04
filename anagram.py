from collections import defaultdict
from collections import Counter
#https://leetcode.com/problems/valid-anagram/
def anagram(s,t):
    
        s_dict=defaultdict(int)
        t_dict=defaultdict(int)
        for i in s:
            s_dict[i]+=1
        for j in t:
            t_dict[j]+=1
        for c in "abcdefghijklmnopqrstuvwxyz":
            if s_dict[c]!=t_dict[c]:
                return False
        return True
def anaram2(s1,s2):
    s1_count=Counter(s1)
    s2_count=Counter(s2)
    for i in "abcdefghijklmnopqrstuvwxyz":
        if s1_count[i]!=s2_count[i]:
            return False
    return True
print(anaram2('rat','trar'))     
print(anagram("rat","tar"))
