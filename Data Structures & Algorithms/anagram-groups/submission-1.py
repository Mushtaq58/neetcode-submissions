class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        hashmap = {}

        for s in strs:
            frequency_string = self.frequency_string_f(s)

            if frequency_string in hashmap:
                hashmap[frequency_string].append(s)
            else:
                hashmap[frequency_string] = [s]
    
        return list(hashmap.values())

    def frequency_string_f(self, s):
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1  # ord(c) gives the ASCII/Unicode number of character c

        frequency_string = ""

        c = 'a'
        for i in freq:
            frequency_string += c + str(i)
            c = chr(ord(c) + 1)

        return frequency_string