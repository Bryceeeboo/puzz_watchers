from itertools import combinations as combs

""" 
Watchers:
- Watchers occupy cells in a grid.
- Watchers can 'see' other watchers that are in the same row, column, or diagonal as them
- The puzzle:
  - Add a specified number of watchers to the grid
  - Once complete, each watcher must be able to 'see' the same number of watchers (specified at the input of the puzzle)
"""
"""
Implementation:
- 1s in cells to indicate presence of a watcher.
- 0s in cells to indicate blank cell.
- Grid will be a list of lists.
"""

class WatcherPuzzle:
    """A class representing the watchers puzzle."""


    """
    Initialises the WatcherPuzzle class.
    Inputs:
        - int gridsize -> The side dimension of the square grid
        - [[int,int]] coords -> List of lists of ints representing coordinates of existing watchers
        - int add -> The number of watchers to add to the grid
        - int seen -> The number of watchers every other watcher in the grid must 'see'
    """
    def __init__(self, gridsize, coords, add, seen):
        
        # Set parameters
        self.gridsize = gridsize
        self.coords = coords
        self.grid = self.make_grid(self.gridsize, coords) # Make the base grid
        self.add = add
        self.seen = seen

        self.print_grid(self.grid)


    """
    Make and return a grid (list of lists) given the grid size and a list of coordinates.
    Inputs:
        - int gridsize -> The side dimension of the square grid
        - [[int,int]] coords -> List of lists of ints representing coordinates of existing watchers
    """
    def make_grid(self, gridsize, coords):

        grid  = [[0 for i in range(gridsize)] for j in range(gridsize)]
        for coord in coords:
            grid[coord[0]][coord[1]] = 1
        return grid


    """
    'Pretty print' a given grid, by printing a row per line
    """
    def print_grid(self, grid):
        
        for row in grid:
            print (row)
        print()


    """
    Return the grid.
    """
    def get_grid(self):
        return self.grid


    """
    Checks whether a given grid configuration is valid. Uses self.seen to check validity.
    Inputs:
        - [[int]] grid -> The grid to be checked
    Outputs:
        - bool isValid -> Whether or not the given board is valid for the problem.
    """
    def grid_is_valid(self, grid):
        
        for i,row in enumerate(grid): # For each row
            for j,cell in enumerate(row): # For each cell in the row
                
                if cell != 0: # The cell has a watcher in it, check for validity
                    row_sum = sum(row) - 1
                    col_sum = sum([grid[x][j] for x in range(self.gridsize)]) - 1
                    
                    right_diag_sum = 0
                    ii = i
                    jj = j
                    while not(ii==self.gridsize-1) and not(jj==0):
                        # Go one back and one down
                        ii += 1 # One down
                        jj -= 1 # One left
                        right_diag_sum += grid[ii][jj]
                    ii = i
                    jj = j
                    while not(ii==0) and not(jj==self.gridsize-1):
                        # Go one up and one right
                        ii -= 1 # One up
                        jj += 1 # One right
                        right_diag_sum += grid[ii][jj]
                    
                    left_diag_sum = 0
                    ii = i
                    jj = j
                    while not(ii==0) and not(jj==0):
                        # Go one left ond one up
                        ii -= 1 # One up
                        jj -= 1 # One left
                        left_diag_sum += grid[ii][jj]
                    ii = i
                    jj = j
                    while not(ii==self.gridsize-1) and not(jj==self.gridsize-1):
                        # Go one right and one down
                        ii += 1 # One down
                        jj += 1 # One right
                        left_diag_sum += grid[ii][jj]
                    
                    if sum([row_sum, col_sum, right_diag_sum, left_diag_sum]) != self.seen:
                        return False
        return True # If all other tests have failed to return false, then return True


    """
    Solves the grid stored in self.grid.
    """
    def solve_grid(self):
        
        self.solutions = []

        # Generate coords of free spaces in the grid, then brute force combinations of those
        # - N choose R where N is the set of free coordinates, and R = self.add
        free_coords = []
        for i in range(len(self.grid)): # For each row
            for j in range(len(self.grid)): # For each cell in the row 
                if self.grid[i][j] == 0: # There is no watcher in the cell
                    free_coords.append([i,j]) # This cell can potentially have a watcher in it
        
        num_solutions_found = 0
        for added_coords in combs(free_coords,self.add): # All combinations of possible watchers
            # Create the board to be tested
            to_be_tested = self.make_grid(self.gridsize, list(added_coords) + self.coords)
            if self.grid_is_valid(to_be_tested): # Check validity of board
                self.solutions.append(to_be_tested)
                num_solutions_found += 1
        
        return self.solutions


"""USER DEFINED PARAMETERS"""
grid_size = 4
coords = [[0,1],[2,3]]
add = 2
seen = 3

"""SOLVE SEQUENCE"""
wp = WatcherPuzzle(grid_size, coords, add, seen)
solutions = wp.solve_grid()
for solution in solutions:
    wp.print_grid(solution)
