import copy
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
    tree = Tree()
    display_grid(starting_condition)
    display_grid(goal_condition)
    print("\nManhattan distance: ", manhattan(starting_condition, goal_condition))
    print("Hamming distance: ", hamming(starting_condition, goal_condition))
    tree.getMoves(starting_condition)


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
    """
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
    """

    # if we want the heuristic to be admissible, then we shouldn't count the blank tile
    for rows in range(3):
        for cols in range(3):
            # if element in position (x,y) in goal state does not match the instance state
            if ((instance[rows][cols] != goal[rows][cols]) and (instance[rows][cols] != 0)): # and is not the blank space
                print("\nElement: ", instance[rows][cols])
                # displacement is calculated from (0,0) top left, where bottom right is (2,2)
                displacement = [(ix, iy) for iy, row in enumerate(goal) for ix, elem in enumerate(row) if
                                elem == instance[rows][cols]]
                # absolute displacement accounting for coordinate system
                manhattan_dist += (abs(rows - displacement[0][0]) + abs(cols - displacement[0][1]))
                print("Location: ", displacement)
    return manhattan_dist



class Node():
    def __init__(self):
        self.fn = 0 # estimated cost of the cheapest path to a goal state that goes through path of n
        self.gn = 0 # cost of reaching n
        self.hn = 0 # estimated cost of reaching goal from state of n
        self.moves = 0
        self.grid = []
        self.path = []

    def calculate_fn(self):
        self.fn = self.gn + self.hn



class Tree():
    def __init__(self):
        self.moves_arr = []

    def getMoves(self, current):
        self.moves_arr = [] # keep track of possible moves from current state
        blank_pos = self.locateBlank(current)
        print("\nBlank position: ", blank_pos)
        self.shiftBlank(blank_pos)
        new_instances = self.expandNewInstances(current, blank_pos)
        print("New instances: ", new_instances)

    def locateBlank(self, current):
        for x in range(3):
            for y in range(3):
                if current[x][y] == 0:
                    return [x, y]

    def shiftBlank(self, blank_pos):
        direction_arr = [[blank_pos[0], blank_pos[1]+1], # up
                         [blank_pos[0], blank_pos[1]-1], # down
                         [blank_pos[0]-1, blank_pos[1]], # left
                         [blank_pos[0]+1, blank_pos[1]]] # right
        for move in direction_arr: # go through all moves and filter those that are valid
            self.validateMove(move)
        print("Valid moves:", self.moves_arr)

    def validateMove(self, move):
        if (0 > move[0] or move[0] > 2) or (0 > move[1] or move[1] > 2):
            return
        else: # blank move is valid
            self.moves_arr.append(move)

    def expandNewInstances(self, current, blank_pos):
        new_instances = [] # array of possible new instances
        for shift_blank in self.moves_arr:
            # create temporary copy of current board state
            temp_board = copy.deepcopy(current)
            # store element that is being swapped with blank
            temp_elem_swap = temp_board[shift_blank[0]][shift_blank[1]]
            # overwrite element with blank
            temp_board[shift_blank[0]][shift_blank[1]] = 0
            # overwrite blank with element
            temp_board[blank_pos[0]][blank_pos[1]] = temp_elem_swap
            # add new instance state to array
            new_instances.append(temp_board)
        return new_instances


if __name__ == "__main__":
    main()
