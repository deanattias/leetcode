class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # # Brute force approach

        # n = len(A)
        # prefix_common_array = [0] * n

        # # Loop through each index to calculate common elements for each prefix
        # for current_index in range(n):
        #     common_count = 0

        #     # Compare elements in A and B within the range of current prefix
        #     for a_index in range(current_index + 1):
        #         for b_index in range(current_index + 1):

        #             # Check if elements match, and count if they do
        #             if A[a_index] == B[b_index]:
        #                 common_count += 1
        #                 break  # Prevent counting duplicates

        #     # Store the count of common elements for the current prefix
        #     prefix_common_array[current_index] = common_count

        # # Return the final list with counts of common elements in each prefix
        # return prefix_common_array

        # # Approach 2: Hash Set Approach

        # n = len(A)
        # prefix_common_array = [0] * n

        # # Initialize sets to store elements from A and B
        # elements_in_A, elements_in_B = set(), set()

        # # Iterate through the elements of both arrays
        # for current_index in range(n):

        #     # Add current elements from A and B to respective sets
        #     elements_in_A.add(A[current_index])
        #     elements_in_B.add(B[current_index])

        #     common_count = 0

        #     # Count common elements between the sets
        #     for element in elements_in_A:
        #         if element in elements_in_B:
        #             common_count += 1

        #     # Store the count of common elements for the current prefix
        #     prefix_common_array[current_index] = common_count

        # # Return the final array with counts of common elements in each prefix
        # return prefix_common_array

        # Approach 3: Single Pass with Frequency Array

        n = len(A)
        prefix_common_array = [0 for _ in range(n)]
        frequency = [0 for _ in range(n + 1)]
        common_count = 0

        # Iterate through the elements of both arrays
        for current_index in range(n):
            # Increment frequency of current elements in A and B
            # Check if the element in A has appeared before (common in prefix)
            frequency[A[current_index]] += 1
            if frequency[A[current_index]] == 2:
                common_count += 1

            # Check if the element in B has appeared before (common in prefix)
            frequency[B[current_index]] += 1
            if frequency[B[current_index]] == 2:
                common_count += 1

            # Store the count of common elements for the current prefix
            prefix_common_array[current_index] = common_count

        # Return the final array with counts of common elements in each prefix
        return prefix_common_array
