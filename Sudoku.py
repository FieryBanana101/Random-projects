sudoku = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
solution_c = 1

# Print the sudoku with special reformatting
def print_result(data):
    global solution_c
    print(f"Solution {solution_c}")
    for k in range(0, 7, 3):
        for i in range(3):
            print(data[i + k][0:3], "|", data[i + k][3:6], "|", data[i + k][6:9])
        print("- " * 34)
    print("-" * 100)
    solution_c += 1


# Find the position in coordinate y,x for the next empty box, start from (0,0) and end at (8,8)
# Iterate for each row first
def find_empty(data: list):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                return y, x
    return None


# Return False or True based on whether can we put the number "num" inside a given coordinate position (y,x)
# inside the sudoku, evaluated using the regular sudoku rules
def isPossible(data: list, num: int, y: int, x: int):
    for i in range(len(data[y])):
        if num == data[y][i]:
            return False

    for k in range(len(data)):
        if num == data[k][x]:
            return False

    tempx = (x // 3) * 3
    tempy = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if num == data[tempy + i][tempx + j]:
                return False
    return True


# solve the sudoku using previous function using brute force by iterating through all element, and backtracking
# if we get stumped on a certain position
def solve(data: list):
    try:
        if find_empty(data) is not None:
            y, x = find_empty(data)
        for num in range(1, 10):
            if isPossible(data, num, y, x):
                data[y][x] = num
                solve(data)
                data[y][x] = 0
    except UnboundLocalError:
        print_result(data)
    # UnboundLocalError will only happen if sudoku is solved (happen because y,x is unassigned),


# so if sudoku is solved print the result
# this is the first time i ever encounter an error which instead give me an advantage lol
# I have a lot of problem doing the recursion, so this is the best i've got, idk if it's optimal

i = 0

while i < 9:
    sudoku[i] = input("Row  " + str(i + 1) + ": ").split(" ")
    if sudoku[i][-1] == "":
        sudoku[i].pop(-1)
    if len(sudoku[i]) != 9:
        print("invalid input, please input nine number for each row")
        continue
    for j in range(9):
        if 0 > int(sudoku[i][j]) or int(sudoku[i][j]) > 9:
            print("invalid input, please enter number from 0-9")
            i -= 1
    for k in range(9):
        sudoku[i][k] = int(sudoku[i][k])
    i += 1

solve(sudoku)

# Everything should be done, but probably need optimization
