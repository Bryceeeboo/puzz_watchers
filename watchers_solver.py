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

    def __init__(self, gridsize, coords, add, seen):
        self.gridsize = gridsize
        self.make_grid(self.gridsize, coords)
        self.add = add
        self.seen = seen

    def make_grid(self, gridsize, coords):
        self.grid = [[0 for i in range(gridsize)] for j in range(gridsize)]
        for coord in coords:
            self.grid[coord[0]][coord[1]] = 1

    def print_grid(self, grid):
        for row in grid:
            print (row)

    def grid_is_valid(self, grid):
        
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                
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
        return True
wp = WatcherPuzzle(4, [[0,2],[1,1],[1,3],[2,2]], 0, 3)
wp.print_grid(wp.grid)
print(wp.grid_is_valid(wp.grid))
