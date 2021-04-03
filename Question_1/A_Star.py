"""
Question 1.3: General solution of the 8-grid using A*

Write a general version of the A* algorithm (using either of the two heuristic
functions described above) to solve a generic version of the 8-grid where the
user can input any start and goal state. (5 marks)

(Hint: can this be done for any generic pair of configurations...?)
"""

starting_condition = [[7,2,4],
                      [5,0,6],
                      [8,3,1]]

goal_condition = [[0,1,2],
                  [3,4,5],
                  [6,7,8]]


def main():
    display_grid(starting_condition)
    display_grid(goal_condition)
    print(manhattan(starting_condition, goal_condition))
    print(hamming(starting_condition, goal_condition))


def display_grid(grid):
    print(grid[0][0],grid[0][1],grid[0][2])
    print(grid[1][0],grid[1][1],grid[1][2])
    print(grid[2][0],grid[2][1],grid[2][2])
    print("\n")


def hamming(instance, goal): # number of blocks out of place
    hamming_dist = 0
    # if we want the heuristic to be admissible, then we shouldn't count the blank tile
    for row in range(3):
        for col in range(3):
            if ((instance[row][col] != goal[row][col]) and (instance[row][col] != 0)):
                hamming_dist += 1
    return hamming_dist


def manhattan(instance, goal): # sum of Manhattan distances between blocks and goal
    manhattan_dist = 0
    # if we want the heuristic to be admissible, then we shouldn't count the blank tile
    for digit in range(1, 9): # hence we only search numbers 1 through 8
        for row in range(3):
            for col in range(3):
                # find position of number in instance state
                if (digit == instance[row][col]):
                    instance_row = row
                    instance_col = col
                # find position of number in goal state
                if (digit == goal[row][col]):
                    goal_row = row
                    goal_col = col
        manhattan_dist += (abs(instance_row - goal_row) + abs(instance_col - goal_col))
    return manhattan_dist


if __name__ == "__main__":
    main()
