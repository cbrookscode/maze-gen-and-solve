import unittest

from src.maze import Maze
from src.graphics import *

class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        test_group_1 = [[12, 10], [5, 4]]
        for test in test_group_1:
            test_maze = Maze(0, 0, test[0], test[1], 10, 10)
            self.assertEqual(
            len(test_maze._cells),
            test[1],
        )
            self.assertEqual(
            len(test_maze._cells[0]),
            test[0],
        )
            

    def test_maze_created_with_zero_rows_or_cols(self):
        test_group_1 = [[0, 5], [5, 0], [0, 0]]
        for test in test_group_1:
            with self.assertRaises(Exception) as context:
                Maze(0, 0, test[0], test[1], 10, 10)
            self.assertEqual(str(context.exception), "Maze cannot have 0 rows or columns when created")
    

    def test_maze_created_with_neg_values_for_rows_or_cols(self):
        test_group_1 = [[-5, 5], [5, -8], [-2, -1]]
        for test in test_group_1:
            with self.assertRaises(Exception) as context:
                Maze(0, 0, test[0], test[1], 10, 10)
            self.assertEqual(str(context.exception), "Maze cannot a negative value for either rows or columns when created")

    
    def test_break_entrance_and_exit(self):
        test_group_1 = [[12, 10], [5, 4]]
        for test in test_group_1:
            win = Window(1500, 1000)
            test_maze = Maze(15, 15, test[0], test[1], 10, 10, win)
            self.assertEqual(test_maze._cells[0][0].has_top_wall, False)
            self.assertEqual(test_maze._cells[-1][-1].has_bottom_wall, False)

if __name__ == "__main__":
    unittest.main()