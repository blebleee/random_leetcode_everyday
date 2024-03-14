class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        if goal != 0:
            d = {}
            d[0] = [-1]
            curr = 0 

            for idx, i in enumerate(nums):
                curr += i 
                if curr not in d:
                    d[curr] = [idx]
                else:
                    d[curr].append(idx)
            
            # print(d)
            # return 4
            for k, v in d.items():
                t = k + goal 
                if t in d:
                    res += len(d[t]) * len(v)

            # return res 
        
        else:
            arr = []
            flag = 1
            c = 0  
            for i in nums:
                if i == 0:
                    if flag == 0:
                        c += 1 
                    else:
                        flag = 0 
                        c = 1
                else:
                    flag = 1 
                    arr.append(c)
                    c = 0

            if flag == 0:
                arr.append(c) 
            
            print(arr)

            for i in arr:
                res += i * (i+1) // 2
        

        return res
            
