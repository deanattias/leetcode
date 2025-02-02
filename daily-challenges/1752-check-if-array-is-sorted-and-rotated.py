class Solution:
    def check(self, nums: List[int]) -> bool:
        # # Approach 1: Brute Force
        # n = len(nums)

        # # Iterate through all possible rotation offsets
        # for rotation_offset in range(n):
        #     check_sorted = []

        #     # Create the rotated array
        #     for index in range(rotation_offset, n):
        #         check_sorted.append(nums[index])
        #     for index in range(rotation_offset):
        #         check_sorted.append(nums[index])

        #     # Check if the constructed array is sorted
        #     is_sorted = True
        #     for index in range(n - 1):
        #         if check_sorted[index] > check_sorted[index + 1]:
        #             is_sorted = False
        #             break

        #     # If sorted, return True
        #     if is_sorted:
        #         return True

        # # If no rotation makes the array sorted, return False
        # return False

        # # Approach 2: Compare with sorted array
        # size = len(nums)

        # # Create a sorted copy of the list
        # sorted_nums = sorted(nums)

        # # Compare the original list with the sorted list, considering all possible rorations
        # for rotation_offset in range(size):
        #     is_match = True
        #     for index in range(size):
        #         if nums[(rotation_offset + index) % size] != sorted_nums[index]:
        #             is_match = False
        #             break
        #     if is_match:
        #         return True
        # return False

        # Approach 3: Find Smallest Element
        n = len(nums)
        if n <= 1:
            return True

        inversion_count = 0

        # For every pair, count the number of inversions
        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                inversion_count += 1

        # Also check between the last and first element due to rotation
        if nums[0] < nums[n - 1]:
            inversion_count += 1

        return inversion_count <= 1
