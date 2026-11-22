class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort_desc = []
        for i in range(len(position)):
            sort_desc.append((position[i], speed[i]))
        sort_desc.sort(reverse = True)
        stack = [] 
        for (p, s) in sort_desc:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)