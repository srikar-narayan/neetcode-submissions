class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in "([{":
                stack.append(b)
            else:
                if stack == []:
                    return False
                if (b == ')' and stack[-1] == '('
                 or b == ']' and stack[-1] == '['
                 or b == '}' and stack[-1] == '{'):
                    del stack[-1]
                else:
                    return False
        return stack == []
            
                



        