class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # # Approach 1: Iteration
        # # Continue removing occurences of 'part' as lon gas it exists in 's'
        # while part in s:
        #     # find the index of the leftmost occurence of 'part'
        #     part_start_index = s.find(part)

        #     # Remove the substring 'part' by concatenating segments before and after 'part'
        #     s = s[:part_start_index] + s[part_start_index + len(part) :]

        #     # Return the updated string after all occurrences are removed
        # return s

        # Approach 2: Stack

        stack = []
        part_length = len(part)

        # Iterate through each character in the string
        for char in s:
            # Push current character to stack
            stack.append(char)

            # If stack size is greated than or equal to the part length, check for match
            if len(stack) >= part_length and self._check_match(
                stack, part, part_length
            ):
                # Pop the characters matching 'part' from the stack
                for _ in range(part_length):
                    stack.pop()

        # Convert stack to string with correct order
        return "".join(stack)

    # Helper functino to check if the pop of the stack matches the 'part'
    def _check_match(self, stack: list, part: str, part_length: int) -> bool:
        # Compare the top 'part_length' elements of the stack with 'part'
        return "".join(stack[-part_length:]) == part
