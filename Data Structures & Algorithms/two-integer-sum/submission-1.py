class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[nums[i]] = i   # nums[i] creates a different key for hashmap/dictionary everytime


    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashing_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]:
            if complement in hashing_map:
                return [hashing_map[complement], i]
            
            hashing_map[nums[i]] = i
    """