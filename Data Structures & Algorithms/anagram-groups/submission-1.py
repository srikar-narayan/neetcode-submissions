class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        grouper = {}
        for s in strs:
            identity = 26*[0]
            for let in s:
                identity[ord(let) - ord('a')] += 1
            identity = tuple(identity)
            grouper[identity] = grouper.get(identity, []) + [s]
        for sublist in grouper.values():
            output.append(sublist)
        return output