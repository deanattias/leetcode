class Solution:
    # Direction vectors: right, left, down, up (matching grid values 1, 2, 3, 4)
    # _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # def minCost(self, grid: List[List[int]]) -> int:
        # # Appraoch 1: Dynamic Programming
        # num_rows, num_cols = len(grid), len(grid[0])

        # # Initialize all cells with max value
        # min_changes = [[float("inf")] * num_cols for _ in range(num_rows)]
        # min_changes[0][0] = 0

        # while True:
        #     # Store previous state to check for convergence
        #     prev_state = [row[:] for row in min_changes]

        #     # Forward pass: check cells coming from left and top
        #     for row in range(num_rows):
        #         for col in range(num_cols):
        #             # Check cell above
        #             if row > 0:
        #                 min_changes[row][col] = min(
        #                     min_changes[row][col],
        #                     min_changes[row - 1][col]
        #                     + (0 if grid[row - 1][col] == 3 else 1),
        #                 )
        #             # Check cell to the left
        #             if col > 0:
        #                 min_changes[row][col] = min(
        #                     min_changes[row][col],
        #                     min_changes[row][col - 1]
        #                     + (0 if grid[row][col - 1] == 1 else 1),
        #                 )
        #     # Backward pass: check cells coming from right and bottom
        #     for row in range(num_rows - 1, -1, -1):
        #         for col in range(num_cols - 1, -1, -1):
        #             # Check cell below
        #             if row < num_rows - 1:
        #                 min_changes[row][col] = min(
        #                     min_changes[row][col],
        #                     min_changes[row + 1][col]
        #                     + (0 if grid[row + 1][col] == 4 else 1),
        #                 )
        #             # Check cell to the right
        #             if col < num_cols - 1:
        #                 min_changes[row][col] = min(
        #                     min_changes[row][col],
        #                     min_changes[row][col + 1]
        #                     + (0 if grid[row][col + 1] == 2 else 1),
        #                 )
        #     # If no changes were made in this iteration, we've found optimal solution
        #     if min_changes == prev_state:
        #         break

        # return min_changes[num_rows - 1][num_cols - 1]

        # Approach 2: Dijkstra's Algorithm

    # Direction vectors: right, left, down, up (matching grid values 1,2,3,4)
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        # Min-heap ordered by cost. Each element is (cost, row, col)
        pq = [(0, 0, 0)]  # Using list as heap, elements are tuples
        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_cost[0][0] = 0

        while pq:
            cost, row, col = heapq.heappop(pq)

            # Skip if we've found a better path to this cell
            if min_cost[row][col] != cost:
                continue

            # Try all four directions
            for d, (dx, dy) in enumerate(self._dirs):
                new_row, new_col = row + dx, col + dy

                # Check if new position is valid
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                    # Add cost=1 if we need to change direction
                    new_cost = cost + (d != (grid[row][col] - 1))

                    # Update if we found a better path
                    if min_cost[new_row][new_col] > new_cost:
                        min_cost[new_row][new_col] = new_cost
                        heapq.heappush(pq, (new_cost, new_row, new_col))

        return min_cost[num_rows - 1][num_cols - 1]
