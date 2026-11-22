class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for c in s:
            if c.isalnum():
                stripped += c.lower()
        return stripped == stripped[::-1]