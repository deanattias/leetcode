class Solution:
    # Helper function to compute the sum of digits of a number
    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    # Approach #1 - Sorting

    # def maximumSum(self, nums: List[int]) -> int:
    #     digit_sum_pairs = []

    #     # Store numbers with their digit sums as pairs
    #     for number in nums:
    #         digit_sum = self.calculate_digit_sum(number)
    #         digit_sum_pairs.append((digit_sum, number))

    #     # Sort based on digit sums, and if equal, by number value
    #     digit_sum_pairs.sort()

    #     max_pair_sum = -1

    #     # Iterate through the sorted array to find the maximum sum of pairs
    #     for index in range(1, len(digit_sum_pairs)):
    #         current_digit_sum = digit_sum_pairs[index][0]
    #         previous_digit_sum = digit_sum_pairs[index - 1][0]

    #         # If two consecutive numbers have the same digit sum
    #         if current_digit_sum == previous_digit_sum:
    #             current_sum = digit_sum_pairs[index][1] + digit_sum_pairs[index - 1][1]
    #             max_pair_sum = max(max_pair_sum, current_sum)

    #     return max_pair_sum

    # Approach 2: Store Maximum Value
    def maximumSum(self, nums: List[int]) -> int:
        result = -1
        # Array to map digit sums to the largest element with that sum
        # (82 to cover all possible sums from 0 to 81)
        digit_mapping = [0] * 82

        for element in nums:
            digit_sum = 0
            # Calculating digit sum
            temp_element = element
            while temp_element:
                # Extract the last digit and add it to digit sum
                temp_element, curr_digit = divmod(temp_element, 10)
                digit_sum += curr_digit

            # Check if there is already an element with the same digit sum
            if digit_mapping[digit_sum] > 0:
                # Update the result if the sum of the current and mapped element is greater
                result = max(result, digit_mapping[digit_sum] + element)

            # Update the mapping to store the larger of the current or previous element for this digit sum
            digit_mapping[digit_sum] = max(digit_mapping[digit_sum], element)

        return result
