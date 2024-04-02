class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i in range(len(s)):
            if s[i] not in d1 and t[i] not in d2:
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]
            
            elif s[i] not in d1 and t[i] in d2:
                return False 
            elif s[i] in d1 and t[i] not in d2:
                return False
            else:
                if d1[s[i]] != t[i] or d2[t[i]] != s[i]:
                    return False
        
        return True