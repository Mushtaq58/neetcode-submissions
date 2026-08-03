class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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