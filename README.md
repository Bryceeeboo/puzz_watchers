# puzz_watchers
Solver for the "Watchers" puzzle.

Puzzle description:
- A square grid with 'watchers', that fill cells of the grid
- Watchers can see other watchers which are in the same row, column, or diagonal as themselves.
- The number of watchers a watcher sees is the sum of the watchers in these visible zones, not counting the watcher itself.

Problem description:
- Given an initial grid consisting of some watchers and some empty spaces.
- Given a number of watchers to ADD.
- Given a number of watchers to SEE.
- Add ADD watchers to the grid, such that every watcher can see SEE other watchers.
