class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            d = i
            while s[d] != '#':
                d += 1
            
            length = s[i:d]
            i = d + 1
            d = i + int(length)
            decoded.append(s[i:d])
            i = d
        return decoded