class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        sett = set()

        longest_length = 0

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            sett.add(s[right])

            window = (right - left) + 1

            longest_length = max(longest_length, window)

        return longest_length