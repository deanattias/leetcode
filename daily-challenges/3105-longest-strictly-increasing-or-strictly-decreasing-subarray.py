class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # # Approach 1: Brute Force
        # max_length = 0

        # # Find longest strictly increasing subarray
        # for start in range(len(nums)):
        #     curr_length = 1
        #     for pos in range(start + 1, len(nums)):
        #         # Extend subarray if next element is larger
        #         if nums[pos] > nums[pos - 1]:
        #             curr_length += 1
        #         else:
        #             # Break if sequence is not increasing anymore
        #             break
        #     max_length = max(max_length, curr_length)

        # # Find longest strictly decreasing subarray
        # for start in range(len(nums)):
        #     curr_length = 1
        #     for pos in range(start + 1, len(nums)):
        #         # Extend subarray if next element is smaller
        #         if nums[pos] < nums[pos - 1]:
        #             curr_length += 1
        #         else:
        #             # Break if sequence is not decreasing anymore
        #             break
        #     max_length = max(max_length, curr_length)

        # return max_length  # Return the longer of increasing or decreasing sequences

        # Appraoch 2: Single Iteration
        # Track current lengths of increasing and decreasing sequences
        inc_length = dec_length = max_length = 1

        # Iterate through array comparing adjacend elements
        for pos in range(len(nums) - 1):
            if nums[pos + 1] > nums[pos]:
                # If next element is larger, extend increasing sequence
                inc_length += 1
                dec_length = 1  # Reset decreasing sequence
            elif nums[pos + 1] < nums[pos]:
                # If next element is smaller, extend decreasing sequence
                dec_length += 1
                inc_length = 1  # Reset increasing sequence
            else:
                # If elements are equal, reset both sequences
                inc_length = dec_length = 1

            # Update max langth considering both sequences
            max_length = max(max_length, inc_length, dec_length)

        return max_length
