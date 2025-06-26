def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Initialize pointer for the place of unique elements
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
