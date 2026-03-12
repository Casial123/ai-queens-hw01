import unittest
import time
from src.queens import solve_n_queens, solve_n_queens_heuristic, compare_algorithms

class TestNQueens(unittest.TestCase):
    def test_4_queens(self):
        self.assertEqual(len(solve_n_queens(4)), 2)

    def test_8_queens(self):
        self.assertEqual(len(solve_n_queens(8)), 92)

    def test_1_queen(self):
        self.assertEqual(len(solve_n_queens(1)), 1)

    def test_heuristic_algorithm(self):
        sol = solve_n_queens_heuristic(8)
        self.assertTrue(len(sol) == 8)
        start = time.time()
        sol_100 = solve_n_queens_heuristic(100)
        self.assertTrue(time.time() - start < 1)
        self.assertTrue(len(sol_100) == 100)

if __name__ == "__main__":
    unittest.main(verbosity=2)