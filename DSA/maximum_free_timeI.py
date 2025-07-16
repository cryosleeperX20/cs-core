    def maxFreeTime(self, eventTime, k, startTime, endTime):
        n = len(startTime)
        
        max_free = 0
        
        for i in range(n - k + 1):
            left_bound = startTime[i] if i > 0 else 0
            right_bound = endTime[i + k - 1] if i + k - 1 < n - 1 else eventTime
            
            if i > 0:
                left_bound = endTime[i - 1]
            if i + k < n:
                right_bound = startTime[i + k]
            
            total_duration = sum(endTime[j] - startTime[j] for j in range(i, i + k))
            free_time = right_bound - left_bound - total_duration
            
            max_free = max(max_free, free_time)
        
        return max_free
