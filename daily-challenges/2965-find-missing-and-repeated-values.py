class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq = {}
        n = len(grid)

        # Store frequency of each number in the grid
        for nums in grid:
            for num in nums:
                freq[num] = freq.get(num, 0) + 1

        # Check numbers from 1 to n^2 to find missing and repeated values
        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num  # Number not present in grid
            elif freq[num] == 2:
                repeat = num  # Number appears twice

        return [repeat, missing]
