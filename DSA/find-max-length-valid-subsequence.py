from typing import List
1    def maximumLength(self, nums: List[int]) -> int:
        count_even = count_odd = 0
        even_end = odd_end = 0

        for num in nums:
            if num % 2 == 0:
                count_even += 1
                even_end = max(even_end, odd_end + 1)
            else:
                count_odd += 1
                odd_end = max(odd_end, even_end + 1)

        same_parity_max = max(count_even, count_odd)
        alt_max = max(even_end, odd_end)
        return max(same_parity_max, alt_max)
