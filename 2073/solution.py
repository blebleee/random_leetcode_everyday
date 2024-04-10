class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        # n = len(tickets)
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    res += 1 
                    tickets[i] -= 1 

                    if i == k and tickets[i] == 0:
                        break
            
            # k -= 1
        
        return res2