class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # implementation
        """
        visit each node from left to right, up to down
        at each node, check value
        if node is a 0, continue
        if node is part of an existingg island, continue
        if node is a 1:
            - run dfs to find all parts of that island and return those nodes
            - increment counter by 1
        continue until r == ROW - 1 and c == COL - 1
        Time complexity: (r * c)
        """

        # DFS base cases
        """
        if we are out of bounds, return 0 (top, left and bottom, right)
        if we are at a 0, return False
        if we are at a point already visited, return False
        if we are at a 1, add that value to the hash set
        """

        result_counter = 0  # count the number of islands
        visited_islands = set() # count the number of visited islands
        ROWS, COLS = len(grid), len(grid[0])    # size of grid
        r, c = 0, 0
        while True:
            # base cases, check implementation
            if (grid[r][c] == "1") and ((r, c) not in visited_islands):
                current_islands = set()
                visited_islands = visited_islands.union(self.matrixDFS(grid, r, c, current_islands))
                result_counter += 1

            # get next island
            c += 1
            if c == COLS:
                r += 1
                if r == ROWS:
                    break
                c = 0
                

        return result_counter


    def matrixDFS(self, grid: List[List[str]], r: int, c: int, visited: set) -> set:
        ROWS, COLS = len(grid), len(grid[0])

        # base case: not island
        if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r, c) in visited:
            return False

        visited.add((r, c))

        self.matrixDFS(grid, r + 1, c, visited)
        self.matrixDFS(grid, r - 1, c, visited)
        self.matrixDFS(grid, r, c + 1, visited)
        self.matrixDFS(grid, r, c - 1, visited)
    
        return visited
        


        












        