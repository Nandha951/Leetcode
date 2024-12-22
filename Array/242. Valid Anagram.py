class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1, hashmap2 = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hashmap1[s[i]] = 1 + hashmap1.get(s[i], 0)
            hashmap2[t[i]] = 1 + hashmap2.get(t[i], 0)
        for value in hashmap1:
            if hashmap1[value] != hashmap2.get(value, 0):
                return False
        return True