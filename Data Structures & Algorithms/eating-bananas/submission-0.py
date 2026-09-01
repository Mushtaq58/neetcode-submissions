from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        result = right

        while left <= right:

            k = (left + right) // 2

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(p / k)

            if totalTime <= h:
                result = k
                right = k - 1
            else:
                left = k + 1

        return result