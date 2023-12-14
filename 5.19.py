from queue import Queue

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]

    def __str__(self):
        result = []
        for row in self.maze:
            result.append(" ".join(row))
        return "\n".join(result)

    def is_valid(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == "0" and not self.visited[row][col]

    def dfs(self, start_row, start_col):
        stack = [(start_row, start_col)]
        while stack:
            row, col = stack.pop()
            if not self.is_valid(row, col):
                continue
            self.visited[row][col] = True
            print(f"Visiting cell ({row}, {col})")
            # Add your processing logic here

            # Explore neighbors in the order of your choice (e.g., up, down, left, right)
            neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for neighbor in neighbors:
                n_row, n_col = neighbor
                if self.is_valid(n_row, n_col):
                    stack.append((n_row, n_col))

    def bfs(self, start_row, start_col):
        q = Queue()
        q.put((start_row, start_col))
        while not q.empty():
            row, col = q.get()
            if not self.is_valid(row, col):
                continue
            self.visited[row][col] = True
            print(f"Visiting cell ({row}, {col})")
            # Add your processing logic here

            # Explore neighbors in the order of your choice (e.g., up, down, left, right)
            neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for neighbor in neighbors:
                n_row, n_col = neighbor
                if self.is_valid(n_row, n_col):
                    q.put((n_row, n_col))

# 예제 미로
maze = [
    ["0", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "1", "0"],
    ["0", "0", "0", "0", "0"]
]

solver = MazeSolver(maze)
print("Maze:")
print(solver)
print("\nDFS:")
solver.dfs(0, 0)
solver.visited = [[False] * solver.cols for _ in range(solver.rows)]  # Reset visited array
print("\nBFS:")
solver.bfs(0, 0)
#이 코드는 미로 탐색을 위한 MazeSolver 클래스를 정의하고, dfs와 bfs 함수를 구현하여
#깊이우선탐색과 너비우선탐색을 수행합니다. 미로 데이터는 maze 변수에 정의되며, 
#visited 배열을 사용하여 방문한 셀을 추적합니다. dfs 및 bfs 함수 내에서 셀 방문을 
#처리하고 이동할 방향을 정의할 수 있습니다. 이 코드를 원하는 미로 데이터와 함께 실행하면 
#해당 미로를 탐색할 수 있습니다.