class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Set the initial color to be replaced
        start_color = image[sr][sc]
        
        # Get the number of rows and columns in the image
        rows,cols = len(image),len(image[0])
        
        # Recursive function to perform flood fill
        def backtrack(i,j,grid):
            # Base case: return if the index is out of bounds
            if i<0 or i>=rows or j<0 or j>=cols:
                return 
        # Base case: return if the current pixel is not the start color or already changed to the new color
            if start_color != grid[i][j] or grid[i][j]==color:
                return
            # Set the color of the current pixel to the new color
            grid[i][j] = color
            # Recursively perform flood fill on the 4-directional neighbors of the current pixel
            backtrack(i-1,j,grid) # up
            backtrack(i,j-1,grid) # left
            backtrack(i+1,j,grid) # down
            backtrack(i,j+1,grid) # right
        
        # Call the backtrack function with the starting pixel and return the modified image
        backtrack(sr,sc,image)
        return image