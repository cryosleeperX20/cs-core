from typing import List
from bisect import bisect_right
from functools import lru_cache

    def maxValue(self, events: List[List[int]], k: int) -> int:
    
        events.sort(key=lambda x: x[1])
        
        end_times = [event[1] for event in events]
        
        @lru_cache(None)
        def dp(i, remaining):
            if i < 0 or remaining == 0:
                return 0
          
            skip = dp(i - 1, remaining)
        
            prev = bisect_right(end_times, events[i][0] - 1) - 1
            take = dp(prev, remaining - 1) + events[i][2]
            return max(skip, take)

        return dp(len(events) - 1, k)
