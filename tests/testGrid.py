import unittest
from model import Grid, Source


class TestGrid(unittest.TestCase):
    def test_grid_creation(self):
        grid = Grid(100, 100)
        self.assertEqual(len(grid), 50, "Correct row size")
        self.assertEqual(len(grid[0]), 50, "Correct column size")

    def test_grid_printing(self):
        grid = Grid(4, 4)
        self.assertEqual (grid[0], [999.0] * 2)
        self.assertEqual (grid[1], [999.0] * 2)

    def test_grid_update(self):
        grid = Grid(4, 4)
        grid[1][1] = 10.0
        self.assertEqual (grid[0], [999.0] * 2)
        self.assertEqual (grid[1], [999.0, 10.0])

    def test_propagate(self):
        grid = Grid(8, 8)
        grid.add_source(Source(2, 1))
        grid.propagate()
        print (grid)
        self.assertEqual(grid[0], [2, 2, 2, 2])
        self.assertEqual(grid[1], [1, 1, 1, 2])
        self.assertEqual(grid[2], [1, 0, 1, 2])
        self.assertEqual(grid[3], [1, 1, 1, 2])

    def test_propagate_short(self):
        grid = Grid(8, 8)
        grid.add_source(Source(2, 1))
        grid.propagate(9)

        self.assertEqual(grid[0], [999.0, 999.0, 999.0, 999.0])
        self.assertEqual(grid[1], [1, 1, 1, 999.0])
        self.assertEqual(grid[2], [1, 0, 1, 999.0])
        self.assertEqual(grid[3], [1, 1, 1, 999.0])



if __name__ == '__main__':
    unittest.main()