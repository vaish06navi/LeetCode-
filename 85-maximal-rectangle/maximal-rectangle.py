class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        maxArea = 0
        
        for row in matrix:
            for j in range(m):
                # Update the histogram heights for each column
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Use the largestRectangleArea method to find the max area for this row
            maxArea = max(maxArea, self.largestRectangleArea(heights))
        
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea


