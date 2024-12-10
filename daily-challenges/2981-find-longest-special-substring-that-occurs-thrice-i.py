def maximumLength(self, s: str) -> int:
    # Track top-3 max substring lengths for each letter ('a' to 'z')
    top3freq = [[-1, -1, -1] for _ in range(26)]

    last_seen = '*'  # Previous character seen during traversal
    win_len = 0  # Current substring length

    for curr in s:
        idx = ord(curr) - ord('a')  # Map character to its index (0-25)

        # Update the current substring length if repeating, else reset
        win_len = win_len + 1 if curr == last_seen else 1
        last_seen = curr

        # Replace the smallest tracked length if current window is longer
        min_index = top3freq[idx].index(min(top3freq[idx]))
        if win_len > top3freq[idx][min_index]:
            top3freq[idx][min_index] = win_len

    # Calculate the maximum of the smallest top-3 lengths across all letters
    return max(min(freq) for freq in top3freq)