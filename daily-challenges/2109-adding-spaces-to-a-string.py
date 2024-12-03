# def addSpaces(s: str, spaces: list[int]) -> str:
#     result = []
#     prev = 0
#     for space in spaces:
#         result.append(s[prev:space])
#         result.append(" ")
#         prev = space
#     result.append(s[prev:])
#     return "".join(result)

# Two-Ptr Approach
def addSpaces(s: str, spaces: list[int]) -> str:
    i, j = 0, 0
    res = []

    while i < len(s) and j < len(spaces):
        if i < spaces[j]:
            res.append(s[i])
            i += 1
        else:
            res.append(" ")
            j += 1

    res.extend(s[i:])

    return "".join(res)





"""
Example 1:

Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"
Explanation:
The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
We then place spaces before those characters.
Example 2:

Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"
Explanation:
The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
We then place spaces before those characters.
Example 3:


Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g"
Explanation:
We are also able to place spaces before the first character of the string.
"""

test_1 = addSpaces("LeetcodeHelpsMeLearn", [8,13,15])
test_2 = addSpaces("icodeinpython", [1,5,7,9])
test_3 = addSpaces("spacing", [0,1,2,3,4,5,6])

assert test_1
print(test_2)
print(test_3)