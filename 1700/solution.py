class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = {}
        for s in students:
            if s not in d:
                d[s] = 1 
            else:
                d[s] += 1 
        
        n = len(sandwiches)
        for s in sandwiches:
            if s not in d or d[s] == 0:
                break 
            
            if n == 0:
                break 
            
            d[s] -= 1 
            n -= 1 
        
        return n