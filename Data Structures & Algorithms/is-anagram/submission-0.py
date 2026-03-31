from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict1 = defaultdict(int)
        mydict2 = defaultdict(int)
        for w in s:
            mydict1[w] += 1
        for w in t:
            mydict2[w] += 1
        if mydict1 != mydict2:
            return False
        return True
            