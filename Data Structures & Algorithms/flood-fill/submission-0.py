class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image
        
        def dfsFloodFill(sr, sc):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != original_color:
                return 

            image[sr][sc] = color

            dfsFloodFill(sr-1, sc)
            dfsFloodFill(sr+1, sc)
            dfsFloodFill(sr, sc-1)
            dfsFloodFill(sr, sc+1)
        
        dfsFloodFill(sr, sc)

        return image