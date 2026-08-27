class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1
            
        if s1_counts == s2_counts:
            return True

        for i in range(n1, n2):
            # Slide the window of already size n1 (because of loop above) across the rest of s2, one character at a time
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i - n1]) - 97] -= 1
            # Remove the character that just fell out of the left side of the window
            if s1_counts == s2_counts:
                return True

        return False