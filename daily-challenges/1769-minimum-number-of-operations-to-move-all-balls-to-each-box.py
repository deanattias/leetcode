class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Approach 1: Brute force
        # n = len(boxes)
        # answer = [0] * n

        # for current_box in range(n):
        #     # If the current box contains a ball, calculate the number of moves for every box.
        #     if boxes[current_box] == '1':
        #         for new_position in range(n):
        #             answer[new_position] += abs(new_position - current_box)
        # return answer

        # Approach 2: Sum of Left and Right Moves
        n = len(boxes)
        answer = [0] * n

        balls_to_left = 0
        moves_to_left = 0
        balls_to_right = 0
        moves_to_right = 0

        # Single pass: calculate moves from both left and right
        for i in range(n):
            # Left pass
            answer[i] += moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left

            # Right pass
            j = n - 1 - i
            answer[j] += moves_to_right
            balls_to_right += int(boxes[j])
            moves_to_right += balls_to_right

        return answer
