class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # # Approach 1: Brute Force (TLE)
        # MOD = 10**9 + 7
        # n = len(arr)
        # count = 0

        # # Generate all possible subarrays
        # for start_index in range(n):
        #     current_sum = 0

        #     # Iterate through each subarray starting at start_index
        #     for end_index in range(start_index, n):
        #         current_sum += arr[end_index]
        #         # Check if the sum is odd
        #         if current_sum % 2 != 0:
        #             count += 1

        # return int(count % MOD)

        # Appraoch 2: Prefix Sum with Odd-Even Counting
        MOD = 10**9 + 7
        count = prefix_sum = 0

        # even_count starts as 1 since the initial sum (0) is even
        odd_count = 0
        even_count = 1

        for num in arr:
            prefix_sum += num
            # If current prefix sum is even, add the number of odd subarrays
            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1

            else:
                # If current prefix sum is odd, add the number of even subarrays
                count += even_count
                odd_count += 1
            count %= MOD  # To handle large results

        return count
