class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouper = {}
        for s in strs:
            identity = 26*[0]
            for let in s:
                identity[ord(let) - ord('a')] += 1
            identity = tuple(identity)
            if identity in grouper:
                grouper[identity].append(s)
            else:
                grouper[identity] = [s]
        return list(grouper.values())