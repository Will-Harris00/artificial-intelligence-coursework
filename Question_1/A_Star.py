"""
Question 1.3: General solution of the 8-grid using A*

Write a general version of the A* algorithm (using either of the two heuristic
functions described above) to solve a generic version of the 8-grid where the
user can input any start and goal state. (5 marks)

(Hint: can this be done for any generic pair of configurations...?)
"""

starting_state = [[7,2,4],
                  [5,0,6],
                  [8,3,1]]

goal_state = [[0,1,2],
              [3,4,5],
              [6,7,8]]


def main():
    display_grid(starting_state)
    display_grid(goal_state)

def display_grid(grid):
    print(grid[0][0],grid[0][1],grid[0][2])
    print(grid[1][0],grid[1][1],grid[1][2])
    print(grid[2][0],grid[2][1],grid[2][2])
    print("\n")

if __name__ == "__main__":
    main()
