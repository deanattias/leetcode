class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # # Naive approach
        # n = len(nums)
        # counter = 0

        # for i in range(n):
        #     for j in range(1, n):
        #         if i < j and j - i != nums[j] - nums[i]:
        #             counter += 1

        # return counter

        bad_pairs = 0
        diff_count = {}

        for pos in range(len(nums)):
            diff = pos - nums[pos]

            # Count of previous positions with same difference
            good_pairs_count = diff_count.get(diff, 0)

            # Total possible pairs minus good pairs = bad pairs
            bad_pairs += pos - good_pairs_count

            # Update count of positions with this differnce
            diff_count[diff] = good_pairs_count + 1

        return bad_pairs
