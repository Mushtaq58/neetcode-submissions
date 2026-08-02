class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [None] * (len(nums) + 1)
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for key in hashmap.keys():
            frequency = hashmap[key]
            if bucket[frequency] is None:
                bucket[frequency] = []
            bucket[frequency].append(key)

        result = [0] * k
        counter = 0

        for pos in range(len(bucket) - 1, -1, -1):
            if counter >= k:
                break
            if bucket[pos] is not None:
                for integer in bucket[pos]:
                    result[counter] = integer
                    counter += 1
        
        return result