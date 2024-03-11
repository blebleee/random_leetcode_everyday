class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d1 = {}
        for i in range(len(order)):
            d1[order[i]] = i
            # d2[i] = order[i] 
        
        d3 = {}
        not_in_order = ''
        res = [''] * len(order)
        print(res)

        for i in s:
            if i in d1:
                if i not in d3:
                    d3[i] = 1 
                else:
                    d3[i] += 1
            
            else:
                not_in_order += i 
        
        for k, v in d3.items():
            print(d1[k])
            res[d1[k]] = k * v 
        
        return ''.join(res) + not_in_order