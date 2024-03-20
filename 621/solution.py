class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        
        max_count  = 0 
        for k, v in d.items():
            max_count = max(max_count, v)
        
        num_max_tasks = 0 
        for k, v in d.items():
            if v == max_count:
                num_max_tasks += 1 
        
        intervals = (max_count - 1) * (n + 1) + num_max_tasks

        return max(intervals, len(tasks))
        