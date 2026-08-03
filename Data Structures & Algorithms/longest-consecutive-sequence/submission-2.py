class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest

        """
        my Solution
        
        if not nums:
            return 0

        nums.sort()

        overall_streak = 1
        curr_streak = 1

        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                i += 1
                continue
            if nums[i] == nums[i - 1] + 1:
                curr_streak += 1
            else:
                curr_streak = 1
            overall_streak = max(overall_streak, curr_streak)
            i += 1

        return overall_streak
        """