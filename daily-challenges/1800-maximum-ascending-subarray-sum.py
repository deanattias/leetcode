class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # # Approach 1: Brute Force
        # max_sum = 0

        # for start_idx in range(len(nums)):
        #     current_subarray_sum = nums[start_idx]

        #     # Inner loop to check the next elements forming an ascending subarray
        #     end_idx = start_idx + 1
        #     while end_idx < len(nums) and nums[end_idx] > nums[end_idx - 1]:
        #         current_subarray_sum += nums[end_idx]
        #         end_idx += 1

        #     # Update max_sum if we find a larger ascending subarray sum
        #     max_sum = max(max_sum, current_subarray_sum)

        # return max_sum

        # Approach 2: Linear Scanning
        max_sum = 0
        current_subarray_sum = nums[0]

        # Loop through the list starting from the second element
        for current_idx in range(1, len(nums)):
            if nums[current_idx] <= nums[current_idx - 1]:
                # If the current element is not greater than the previous one, update max_sum
                max_sum = max(max_sum, current_subarray_sum)
                # Reset the sum for the ascending subarray
                current_subarray_sum = 0
            current_subarray_sum += nums[current_idx]

        # Final check after the loop ends to account for the last ascending subarray
        return max(max_sum, current_subarray_sum)
