class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # # Iterate over integer equivalents
        # integers = set()
        # for num in nums:
        #     integers.add(int(num, 2))

        # n = len(nums)
        # for num in range(n + 1):
        #     if num not in integers:
        #         ans = bin(num)[2:]
        #         return "0" * (n - len(ans)) + ans

        # return ""

        # Cantor's Diagonal Argument
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")
        return "".join(ans)
