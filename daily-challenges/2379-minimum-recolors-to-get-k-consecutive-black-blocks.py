class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # # Approach 1: Queue
        # block_queue = deque()
        # num_whites = 0

        # # Initiate queue with first k values
        # for i in range(k):
        #     current_char = blocks[i]
        #     if current_char == "W":
        #         num_whites += 1
        #     block_queue.append(current_char)

        # # Set initial minimum
        # num_recolors = num_whites

        # for i in range(k, len(blocks)):

        #     # Remove front element from queue and update current number of white blocks
        #     if block_queue.popleft() == "W":
        #         num_whites -= 1

        #     # Add current element to queue and update current number of white blocks
        #     current_char = blocks[i]
        #     if current_char == "W":
        #         num_whites += 1
        #     block_queue.append(current_char)

        #     # Update minimum
        #     num_recolors = min(num_recolors, num_whites)

        # return num_recolors

        # Approach 2: Sliding Window
        left = 0
        num_whites = 0
        num_recolors = float("inf")

        # Move right pointer
        for right in range(len(blocks)):
            # Increment num_whites if block at right pointer is white
            if blocks[right] == "W":
                num_whites += 1

            # k consecutive elements are found
            if right - left + 1 == k:
                # Update minimum
                num_recolors = min(num_recolors, num_whites)

                # Decrement num_whites if block at left pointer is white
                if blocks[left] == "W":
                    num_whites -= 1

                # Move left pointer
                left += 1

        return num_recolors
