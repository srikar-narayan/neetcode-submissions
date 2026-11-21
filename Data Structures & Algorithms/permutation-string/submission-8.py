class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1 = {}
        set2 = {}
        for ind in range(len(s1)):
            set1[s1[ind]] = 1 + set1.get(s1[ind], 0)
        l = 0
        r = len(s1) - 1
        print(set1)
        while r < len(s2):
            for ind in range(l, r + 1):
                set2[s2[ind]] = 1 + set2.get(s2[ind], 0)
            print(set2)
            if set1 == set2:
                return True
            set2 = {}
            l += 1
            r += 1
        return False

        


        