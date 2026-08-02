class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False