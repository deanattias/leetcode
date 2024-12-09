class Solution:
    def isArraySpecial(nums: list[int], queries: list[list[int]]) -> list[bool]:
        # # O(m * n)
        # def is_special(from_i: int, to_i):
        #     for i in range(from_i, to_i):
        #         if nums[i] % 2 == nums[i + 1] % 2:
        #             return False
        #     return True

        # answer = []
        # for from_i, to_i in queries:
        #     if from_i == to_i:
        #         answer.append(True)
        #     else:
        #         answer.append(is_special(from_i, to_i))

        # return answer

        # O(m + n)
        n = len(nums)

        # Step 1: Precompute where the array is "not special"
        not_special = [0] * n

        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                not_special[i] = 1

        # Step 2: Build prefix sums for fast range checking
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + not_special[i]

        # Step 3: Answer each query
        result = []
        for from_i, to_i in queries:
            if from_i == to_i:
                result.append(True)
            else:
                has_issue = prefix_sum[to_i] - prefix_sum[from_i]
                result.append(has_issue == 0)

        return result
