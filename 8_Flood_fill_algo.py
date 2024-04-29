class Solution:
    def is_valid(self, image, x, y, M, N, old_col, new_col):
        return 0 <= x < M and 0 <= y < N and image[x][y] == old_col and image[x][y] != new_col

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M = len(image)
        N = len(image[0])
        old_color = image[sr][sc]
        if old_color == color: return image

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        queue = [(sr, sc)]
        image[sr][sc] = color
        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                if self.is_valid(image, newX, newY, M, N, old_color, color):
                    image[newX][newY] = color
                    queue.append((newX, newY))
        return image
