class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency_map = [0] * 26

        for char in s:
            frequency_map[ord(char) - ord('a')] += 1

        for char in t:
            frequency_map[ord(char) - ord('a')] -= 1

        for count in frequency_map:
            if count != 0:
                return False

        return True
    """