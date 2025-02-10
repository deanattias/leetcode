class Solution:
    def clearDigits(self, s: str) -> str:
        # # Approach 1: Brute force TC: (O(m x n)) or O(n^2))
        # s = list(s)
        # char_index = 0

        # # Until we reach the end of the string
        # while char_index < len(s):
        #     if s[char_index].isdigit():
        #         # Remove the digit from the string
        #         del s[char_index]
        #         # If there is a character to the left of the digit, remove it
        #         if char_index > 0:
        #             del s[char_index - 1]
        #             # Adjust the index to account for the removed character
        #             char_index -= 1
        #     else:
        #         # Move to the next character if it's not a digit
        #         char_index += 1

        # return "".join(s)

        # # Approach 2: Stack-like TC: O(n):
        # # Use a list to store characters for efficient modification
        # answer = []

        # # Iterate over each character in the input string
        # for char in s:
        #     # If the current character is a digit
        #     if char.isdigit() and answer:
        #         # If the answer list is not empty, remove the last character
        #         answer.pop()
        #     else:
        #         # If the character is not a digit, add it to the answer list
        #         answer.append(char)
        # # Join the list back into a string before returning
        # return "".join(answer)

        # Approach 3: In-place
        # This variable keeps track of the actual length of the resulting string
        answer_length = 0
        s = list(s)
        n = len(s)

        # Iterate through each character in the input string
        for char_index in range(n):
            # If the current character is a digit
            if s[char_index].isdigit():
                # Decrement answer_length to remove the last character from the result
                answer_length = max(answer_length - 1, 0)
            else:
                # Place the character in the "answer" portion of the string
                s[answer_length] = s[char_index]
                answer_length += 1

        # Resize the string to match the actual length of the answer
        s = s[:answer_length]

        return "".join(s)
