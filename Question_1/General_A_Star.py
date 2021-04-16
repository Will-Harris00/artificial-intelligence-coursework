import A_Star
import Parity

"""
Question 1.3: General solution of the 8-puzzle using A*

Write a general version of the A* algorithm (using either of the two heuristic
functions described above) to solve a generic version of the 8-grid where the
user can input any start and goal state. (5 marks)

(Hint: can this be done for any generic pair of configurations...?)
"""


def get_input():
    while True:
        print("Example '012345678' would be state")
        A_Star.display_grid([[0,1,2],[3,4,5],[6,7,8]])
        start_state = input("Enter the start state as a single string containing "
                            "nine unique integer values in the range 0-8 where "
                            "'0' is a placeholder for the blank tile:\n")

        if sorted(start_state) == sorted('012345678'):
            break
        else:
            print("Invalid board state!")
    while True:
        goal_state = input("\nNow enter the goal state following the same format:\n")

        if (sorted(start_state) == sorted('012345678') and
            start_state != goal_state):
            break
        elif start_state == goal_state:
            print("The initial and goal state cannot be the same!")
        else:
            print("Invalid board state!")

    A_Star.starting_condition = set_state(start_state)
    A_Star.goal_condition = set_state(goal_state)

    print("\nInitial state\n")
    A_Star.display_grid(A_Star.starting_condition)

    print("Goal state\n")
    A_Star.display_grid(A_Star.goal_condition)


def set_state(state):
    i = 0
    matrix = [[],[],[]]
    for row in range(3):
        for col in range(3):
            matrix[row].append(int(state[i]))
            i += 1
    return matrix

if __name__ == '__main__':
    get_input()
    if (Parity.is_solvable(A_Star.starting_condition, A_Star.goal_condition)):
        A_Star.main()
    else:
        exit(-1)
