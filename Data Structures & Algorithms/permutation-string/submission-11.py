class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1, map2 = 26*[0], 26*[0]
        if len(s1) > len(s2):
            return False
        for ind in range(len(s1)):
            map1[ord(s1[ind]) - 97] += 1

        for ind in range(len(s1)):
            map2[ord(s2[ind]) - 97] += 1
        print(map1)
        print(map2)

        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:
            if map1 == map2:
                return True
            map2[ord(s2[l]) - 97] -= 1
            map2[ord(s2[r+1]) - 97] += 1
            print(map2)
            l += 1
            r += 1
        return map1 == map2

        


        