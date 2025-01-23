class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # # Brute force approach
        # num_rows = len(grid)
        # num_cols = len(grid[0]) if num_rows > 0 else 0
        # communicable_servers_count = 0

        # # Traverse through the grid
        # for row in range(num_rows):
        #     for col in range(num_cols):
        #         if grid[row][col] == 1:
        #             can_communicate = False

        #             # Check for communication in the same row
        #             for other_col in range(num_cols):
        #                 if other_col != col and grid[row][other_col] == 1:
        #                     can_communicate = True
        #                     break

        #             # If a servers was found in the same row,
        #             # increment communicable_server_count
        #             if can_communicate:
        #                 communicable_servers_count += 1
        #             else:
        #                 # Check for communication in the same column
        #                 for other_row in range(num_rows):
        #                     if other_row != row and grid[other_row][col] == 1:
        #                         can_communicate = True
        #                         break

        #                 # If a server was found in the same column, increment
        #                 # communicable_servers_count
        #                 if can_communicate:
        #                     communicable_servers_count += 1

        # return communicable_servers_count

        # Server grouping approach
        communicable_servers_count = 0
        row_counts = [0] * len(grid[0])
        last_server_in_col = [-1] * len(grid)

        # First pass to count servers in each row and column
        for row in range(len(grid)):
            server_count_in_row = 0
            for col in range(len(grid[0])):
                if grid[row][col]:
                    server_count_in_row += 1
                    row_counts[col] += 1
                    last_server_in_col[row] = col

            # If there is more than one server in the row, increase the count
            if server_count_in_row != 1:
                communicable_servers_count += server_count_in_row
                last_server_in_col[row] = -1

        # Second pass to check if servers can communicate
        for row in range(len(grid)):
            if (
                last_server_in_col[row] != -1
                and row_counts[last_server_in_col[row]] > 1
            ):
                communicable_servers_count += 1
        return communicable_servers_count
