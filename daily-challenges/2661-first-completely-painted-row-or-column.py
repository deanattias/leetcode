class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # # Brute force appraoch
        # num_rows, num_cols = len(mat), len(mat[0])
        # row_count, col_count = [0] * num_rows, [0] * num_cols
        # num_to_pos = {}

        # # Create a map to store the position of each number in the matrix
        # for row in range(num_rows):
        #     for col in range(num_cols):
        #         num_to_pos[mat[row][col]] = [row, col]

        # for i in range(len(arr)):
        #     num = arr[i]
        #     row, col = num_to_pos[num]

        #     # Increment the count for the corresponding row and column
        #     row_count[row] += 1
        #     col_count[col] += 1

        #     # Check if the row or column is completely painted
        #     if row_count[row] == num_cols or col_count[col] == num_rows:
        #         return i

        # # This line will neber be reach as per the problem statement
        # return -1

        # Reverse Mapping Apparoch

        # Map to store the index of each number in the arr
        num_to_index = {}
        for i in range(len(arr)):
            num_to_index[arr[i]] = i

        result = float("inf")
        num_rows, num_cols = len(mat), len(mat[0])

        # Check for the earliest row to be completely painted
        for row in range(num_rows):
            # Tracks the greatest index in this row
            last_element_index = float("-inf")
            for col in range(num_cols):
                index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)

            # Update result with the minimum index where this row is fully painted
            result = min(result, last_element_index)

        # Check for the earliest column to be completely painted
        for col in range(num_cols):
            last_element_index = float("-inf")
            for row in range(num_rows):
                index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)

            # Update result with the minimum index where this column is fully painted
            result = min(result, last_element_index)

        return result
