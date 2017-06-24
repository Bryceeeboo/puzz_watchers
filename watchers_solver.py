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
