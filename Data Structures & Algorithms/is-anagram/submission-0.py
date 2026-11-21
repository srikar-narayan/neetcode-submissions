class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount, tcount = {}, {}
        for i in s:
            scount[i] = 1 + scount.get(i, 0)
        for i in t:
            tcount[i] = 1 + tcount.get(i, 0)
        return scount == tcount