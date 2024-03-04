class Solution:
    def bagOfTokensScore(self, tokens: List[int], p: int) -> int:
        tokens.sort()
        s = 0 
        maxx = 0
        l, r = 0, len(tokens) - 1 

        while l <= r:
            if p >= tokens[l]:
                p -= tokens[l]
                s += 1 
                l += 1 
                maxx = max(maxx, s)
            elif s > 0:
                p += tokens[r]
                s -= 1 
                r -= 1 
            else:
                break 
        
        return maxx
