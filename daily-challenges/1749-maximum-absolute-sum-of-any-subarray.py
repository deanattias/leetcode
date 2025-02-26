class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # # Brute Force Approach - O(n^2)
        # n = len(nums)
        # max_sum = float("-inf")
        # for start_index in range(n):
        #     running_sum = 0
        #     for end_index in range(start_index, n):
        #         running_sum += nums[end_index]
        #         abs_sum = abs(running_sum)
        #         max_sum = max(max_sum, abs_sum)
        # return max_sum

        # Optimized Approach: Kadane's Algorithm - O(n)
        max_sum = 0  # Maximum positive subarray sum
        min_sum = 0  # Minimum negative subarray sum
        curr_max = 0
        curr_min = 0

        for num in nums:
            curr_max = max(num, curr_max + num)
            curr_min = min(num, curr_min + num)
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, abs(min_sum))
