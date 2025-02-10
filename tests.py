import unittest

from src.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        test_group_1 = [[12, 10], [0, 5], [5, 0], [0, 0], [-3, 4], [4, -3], [-4, -4]]
        testlist = []
        for test in test_group_1:
            i = Maze(0, 0, test[0], test[1], 10, 10)
            testlist.append(i)

        for i in range(len(testlist)):
            self.assertEqual(
            len(testlist[i]._cells),
            test_group_1[i][1],
        )
        for i in range(len(testlist)):
            self.assertEqual(
            len(testlist[i]._cells[0]),
            test_group_1[i][0],
        )
# need to account for negative and 0 values in creation of maze. not sure how to handle yet. if should allow and change to abs value so its positive always or to raise exceptions and handle via errors.
if __name__ == "__main__":
    unittest.main()