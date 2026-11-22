class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            elif c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                tmp = stack.pop()
                stack.append(stack.pop() - tmp)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                tmp = stack.pop()
                stack.append(int(stack.pop() / tmp))
        return stack.pop()
                




        