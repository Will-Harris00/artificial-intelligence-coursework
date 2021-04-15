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
    heuristic = getHeuristicChoice()
    puzzle = Puzzle(heuristic)
    puzzle.solve()
    """
    board = Board()
    display_grid(starting_condition)
    display_grid(goal_condition)
    print("\nManhattan distance: ", manhattan(starting_condition, goal_condition))
    print("Hamming distance: ", hamming(starting_condition, goal_condition))
    board.getMoves(starting_condition)
    """


def getHeuristicChoice():
    print("Selections:"
          "\n1: Hamming Distance (Count number of displaced tiles)"
          "\n2: Manhattan Distance (Count taxicab distance of displaced tiles)")
    while True:
        heuristic = input("\n")
        try:
            heuristic = int(heuristic)
        except:
            print("Selection must be an integer number")
            continue
        if heuristic == 1:
            break
        elif heuristic == 2:
            break

        print('Please enter a valid number')
        continue
    return heuristic


def display_grid(grid):
    print(grid[0][0],grid[0][1],grid[0][2])
    print(grid[1][0],grid[1][1],grid[1][2])
    print(grid[2][0],grid[2][1],grid[2][2])
    print("\n")


def selectHeuristic(heuristic, instance, goal):
    if heuristic == 1:
        heuristic_dist = hamming(instance, goal)
    elif heuristic == 2:
        heuristic_dist = manhattan(instance, goal)
    return heuristic_dist


def hamming(instance, goal): # number of blocks out of place
    hamming_dist = 0
    # if we want the heuristic to be admissible, then we shouldn't count the blank tile
    for row in range(3):
        for col in range(3):
            if ((instance[row][col] != goal[row][col]) and (instance[row][col] != 0)):
                hamming_dist += 1
    # print("Ham dist:", hamming_dist)
    return hamming_dist


def manhattan(instance, goal): # sum of Manhattan distances between blocks and goal
    manhattan_dist = 0
    # print("Instance:",instance)
    # print("Goal:",goal)

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
                # print("\nElement: ", instance[rows][cols])
                # displacement is calculated from (0,0) top left, where bottom right is (2,2)
                displacement = [(ix, iy) for iy, row in enumerate(goal) for ix, elem in enumerate(row) if
                                elem == instance[rows][cols]]
                # absolute displacement accounting for coordinate system
                manhattan_dist += (abs(rows - displacement[0][0]) + abs(cols - displacement[0][1]))
                # print("Location: ", displacement)
    """
    # print("Man dist:", manhattan_dist)
    return manhattan_dist


def checkQueue(next_path, Queue):
    for node in Queue:
        if next_path.state == node.state and node.fn >= next_path.fn:
            return False
    return True


def getNodeFn(node):
    return node.fn



class Node():
    def __init__(self, state, hn=0, gn=0, moves=0, path=None):
        if path is None:
            path = []
        self.fn = 0 # estimated cost of the cheapest path to a goal state that goes through path of n
        self.gn = gn # cost of reaching n
        self.hn = hn # estimated cost of reaching goal from state of n
        self.moves = moves
        self.state = state # initialise the node with a puzzle board state
        self.path = path

    def calculate_fn(self):
        self.fn = self.gn + self.hn



class Board():
    def __init__(self):
        self.moves_arr = []
        self.blank_pos = []

    def getMoves(self, current):
        self.moves_arr = [] # keep track of possible moves from current state
        self.locateBlank(current)
        print("\nBlank position: ", self.blank_pos)
        self.shiftBlank()
        self.new_instances = self.expandNewInstances(current)
        # print("New instances:",self.new_instances)

    def locateBlank(self, current):
        for x in range(3):
            for y in range(3):
                if current[x][y] == 0:
                    self.blank_pos = [x,y]

    def shiftBlank(self):
        direction_arr = [[self.blank_pos[0]-1, self.blank_pos[1]], # left
                         [self.blank_pos[0], self.blank_pos[1]-1], # down
                         [self.blank_pos[0], self.blank_pos[1]+1], # up
                         [self.blank_pos[0]+1, self.blank_pos[1]]] # right
        for move in direction_arr: # go through all moves and filter those that are valid
            self.validateMove(move)
        # print("Valid moves:",self.moves_arr)

    def validateMove(self, move):
        if (0 > move[0] or move[0] > 2) or (0 > move[1] or move[1] > 2):
            return
        else: # blank move is valid
            self.moves_arr.append(move)

    def expandNewInstances(self, current):
        new_instances = [] # array of possible new instances
        for shift_blank in self.moves_arr:
            # create temporary copy of current board state
            temp_board = copy.deepcopy(current)
            # store element that is being swapped with blank
            temp_elem_swap = temp_board[shift_blank[0]][shift_blank[1]]
            # overwrite element with blank
            temp_board[shift_blank[0]][shift_blank[1]] = 0
            # overwrite blank with element
            temp_board[self.blank_pos[0]][self.blank_pos[1]] = temp_elem_swap
            # add new instance state to array
            new_instances.append(temp_board)
        return new_instances



class Puzzle():
    def __init__(self, heuristic):
        self.heuristic = heuristic
        self.search_state = starting_condition
        self.goal_state = goal_condition

        self.parent = 0
        self.gn = 0

        self.search_nodes = []
        self.evaluated_nodes = []
        self.nodes_considered = 0

    def initialise(self):
        # evaluate initial state of puzzle
        self.hn = selectHeuristic(self.heuristic, self.search_state, self.goal_state)
        print("Value of h(n):", self.hn)
        node = Node(self.search_state)
        node.hn = self.hn
        node.gn = -1
        self.search_nodes.append(node)

    def isExhausted(self):
        # print("Queue:",self.search_nodes)
        # print(self.search_nodes[0].state)
        # print(self.search_nodes[0].fn)
        # print(self.search_nodes[0].hn)
        # print(self.search_nodes[0].gn)
        # print("Evaluated:",self.evaluated_nodes)
        # print("Num considered:",self.nodes_considered)
        if ((len(self.search_nodes) == 0 or
            (len(self.evaluated_nodes) > self.nodes_considered))):
            print("A* search exhausted")
            return True

    def pathNode(self):
        # set path node for first board node in search array
        self.path_node = Node(self.search_nodes[0].state,
                         self.search_nodes[0].hn,
                         self.search_nodes[0].gn,
                         self.search_nodes[0].moves,
                         self.search_nodes[0].path)
        self.path_node.calculate_fn()

    def getStats(self):
        print("\nEvaluate path node:")
        print("Estimated cost f(n) value: ", self.search_nodes[0].fn)
        print("Heuristic h(n) value: ", self.search_nodes[0].hn)
        print("Depth g(n) value: ", self.search_nodes[0].gn)
        display_grid(self.path_node.state)

    def markAsEvaluated(self):
        current_node = self.search_nodes[0]
        self.evaluated_nodes.append(current_node)
        self.search_nodes.pop(0)

    def isPresent(self, node):
        for evald_node in self.evaluated_nodes:
            if node == evald_node.state:
                return True

    def walkthrough(self):
        self.path_node.path.append(self.goal_state)
        print("Puzzle Solved \n")
        print("In moves: ", self.path_node.moves)
        print("Depth: ", self.path_node.gn)
        print("Nodes visited:", len(self.evaluated_nodes))
        print("Total nodes generated: ", self.nodes_considered)
        print("List of moves:\n")
        for path_parent in self.path_node.path:
            display_grid(path_parent)
        exit(0)

    def solve(self):
        board = Board()
        self.initialise()

        while True:
            if (self.isExhausted()):
                exit(0)

            self.pathNode() # generate the next node to be evaluated
            self.getStats() # print latest heuristic information
            self.markAsEvaluated() # move evaluated node to completed array

            if (self.path_node.state == self.goal_state):
                self.walkthrough()

            board.getMoves(self.path_node.state)
            for node in board.new_instances:
                if self.isPresent(node):
                    continue

                next_path = Node(node)
                # print(self.heuristic)
                # print(next_path.state)
                # print(self.goal_state)

                next_path.hn = selectHeuristic(self.heuristic, next_path.state, self.goal_state)
                next_path.gn = self.path_node.gn + 1
                next_path.moves = self.path_node.moves + 1
                next_path.path = copy.deepcopy(self.path_node.path)
                next_path.path.append(self.path_node.state)
                next_path.calculate_fn()

                if checkQueue(next_path, self.search_nodes):
                    self.search_nodes.append(next_path)
                    self.nodes_considered += 1

            self.search_nodes.sort(key=getNodeFn)


if __name__ == "__main__":
    main()
