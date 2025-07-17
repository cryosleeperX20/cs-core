 def maximumLength(self, nums, k):
        n = len(nums)
        max_length = 1 

        for mod in range(k):  
            dp = [1] * n  

            for i in range(n):
                for j in range(i):
                  
                    if (nums[j] + nums[i]) % k == mod:
                        dp[i] = max(dp[i], dp[j] + 1)

            max_length = max(max_length, max(dp))  # Update global max

        return max_length
