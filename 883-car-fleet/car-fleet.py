class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car can not pass = > catch up other car -- > same speed as the car ahead of it
        # same position & same speed == > car fleet

        pair = [(p,s) for p,s in zip(position,speed)]

        pair.sort(reverse = True)
        stack = []

        for p,s in pair: #reverse sorted order
            stack.append((target - p) /s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)