class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        sett = set()

        longest_length = 0

        for right in range(len(s)):

            # If the character is already in the set, we have a duplicate.
            # We must shrink the window from the left until the duplicate is gone.
            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            # Add new element to the set.
            sett.add(s[right])

            window = (right - left) + 1

            longest_length = max(longest_length, window)

        return longest_length