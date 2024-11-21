def countUnguarded(
    m: int, n: int, guards: list[list[int]], walls: list[list[int]]
) -> int:
    # Define grid states
    FREE, GUARD, WALL, GUARDED = 0, 1, 2, 3
    grid = [[FREE] * n for _ in range(m)]

    # Mark guards and walls
    for r, c in guards:
        grid[r][c] = GUARD
    for r, c in walls:
        grid[r][c] = WALL

    # Helper function to mark guarded cells
    def mark_guarded(r, c):
        # Mark downward
        for row in range(r + 1, m):
            if grid[row][c] in [GUARD, WALL]:
                break
            grid[row][c] = GUARDED
        # Mark upward
        for row in reversed(range(0, r)):
            if grid[row][c] in [GUARD, WALL]:
                break
            grid[row][c] = GUARDED
        # Mark rightward
        for col in range(c + 1, n):
            if grid[r][col] in [GUARD, WALL]:
                break
            grid[r][col] = GUARDED
        # Mark leftward
        for col in reversed(range(0, c)):
            if grid[r][col] in [GUARD, WALL]:
                break
            grid[r][col] = GUARDED

    # Mark all guarded cells
    for r, c in guards:
        mark_guarded(r, c)

    # Count unguarded cells
    return sum(cell == FREE for row in grid for cell in row)


test_1 = countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]])
test_2 = countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]])

print(test_1)
print(test_2)   
