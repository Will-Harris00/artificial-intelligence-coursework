# program to check if a given pair of states of an 8 puzzle are solvable or not

# A utility function to count
# inversions in given array 'arr[]'
class Inversions():
    def get_inv_count(self, arr):
        self.inv_count = 0
        for r in range(0, 3): # rows
            for c in range(0, 3): # columns
                current_element = arr[r][c] # assigned element for comparison
                for search_r in range(r, 3): # continue search from current row
                    if ( search_r == r ): # continue from current column in current row
                        for search_c in range(c, 3): # search columns to the right of current cell
                            test_element = arr[search_r][search_c]
                            self.check_inversion(current_element, test_element)
                    else: # start from leftmost column of new row
                        for search_c in range(0, 3): # search all columns
                            test_element = arr[search_r][search_c]
                            self.check_inversion(current_element, test_element)

        return self.inv_count

    def check_inversion(self, current, test):
        # print("\nCurrent:", current)
        # print("Test:", test)
        # Value 0 is used for empty space
        if (test == 0 or current == 0):
            # print("Skip blank tile")
            return
        elif ((0 > test or test > 8) or (0 > current or current > 8)):
            print("Invalid values")
            exit(-1)
        elif(current > test):
            # print("Increment: ", current, " > ", test)
            self.inv_count += 1


# This function returns true
# if given 8 puzzle is solvable.
def check_parity(puzzleInitial, puzzleGoal):
    # Count inversions in given 8 puzzle
    puzzle = Inversions()
    invCountInitial = puzzle.get_inv_count(puzzleInitial)
    invCountGoal = puzzle.get_inv_count(puzzleGoal)
    # print("Inversion count initial:", invCountInitial)
    # print("Inversion count goal:", invCountGoal)
    # return true if goal and initial inversion count are both even or both odd.
    return ((invCountInitial % 2) == (invCountGoal % 2))

# puzzleInitial = [[1, 8, 2], [0, 4, 3], [7, 6, 5]] # 0 inversions: Even
# puzzleGoal = [[1, 8, 2], [0, 4, 3], [7, 6, 5]] # Solvable 10 inversions: Even
# puzzleGoal = [[8, 1, 2],[0, 4, 3],[7, 6, 5]] # Not solvable 11 inversions: Odd
# 1 8 2
# 0 4 3
# 7 6 5

# 8 1 2
# 0 4 3
# 7 6 5

puzzleInitial = [[2,8,3], [1,6,4], [7,0,5]] # Init. Inversion Count: 11 -> odd
puzzleGoal = [[1,2,3], [8,0,4], [7,6,5]] # One. Inversion Count: 7 -> odd <- Solvable
puzzleGoal = [[0,1,2], [3,4,5], [6,7,8]] # Two. Inversion Count: 0 -> even <- Not Solvable
def is_solvable(puzzleInitial, puzzleGoal):
    if (check_parity(puzzleInitial, puzzleGoal)):
        print("Solvable\n")
        return True
    else:
        print("Not Solvable\n")
        return False
