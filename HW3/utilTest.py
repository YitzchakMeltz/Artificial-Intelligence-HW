import unittest
from util import *

HUMAN = 1
COMPUTER = 5

# =================== Empty Board ===================
class TestZeroConsq(unittest.TestCase):
    def test1(self):
        b0 = [[0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(iter_matrix(HUMAN, b0, 2, 1), 0, "Expected result is 0")
        self.assertEqual(iter_matrix(HUMAN, b0, 3, 1), 0, "Expected result is 0")
        self.assertEqual(iter_matrix(HUMAN, b0, 4, 1), 0, "Expected result is 0")
        self.assertEqual(iter_matrix(COMPUTER, b0, 2, 1), 0, "Expected result is 0")
        self.assertEqual(iter_matrix(COMPUTER, b0, 3, 1), 0, "Expected result is 0")
        self.assertEqual(iter_matrix(COMPUTER, b0, 4, 1), 0, "Expected result is 0")
# ===================================================

# ================= Two Consecutive =================
class TestTwoConsq(unittest.TestCase):
    # 4 cases
    def test1(self):
        b1 = [[0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 5, 0, 0, 0], 
              [0, 1, 0, 1, 5, 0, 0], 
              [0, 1, 5, 1, 1, 5, 5]]
        self.assertEqual(iter_matrix(HUMAN, b1, 2, 1), 2, "Expected result is 2")
    def test2(self):
        b1 = [[0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 5, 0, 0, 0], 
              [0, 1, 0, 1, 5, 0, 0], 
              [0, 1, 5, 1, 1, 5, 5]]
        self.assertEqual(iter_matrix(COMPUTER, b1, 2, 1), 1, "Expected result is 1")
# ===================================================

# ================= Two Consecutive =================
class TestThreeConsq(unittest.TestCase):
    # 4 cases
    def test1(self):
        b1 = [[0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 1, 0, 0, 0], 
              [0, 1, 0, 5, 0, 0, 0], 
              [0, 1, 0, 1, 5, 0, 0], 
              [1, 1, 5, 1, 1, 5, 5]]
        self.assertEqual(iter_matrix(HUMAN, b1, 3, 1), 2, "Expected result is 2")
    def test2(self):
        b1 = [[0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 5, 5, 5, 0, 0], 
              [0, 1, 1, 1, 5, 0, 0], 
              [0, 1, 5, 1, 1, 5, 5]]
        self.assertEqual(iter_matrix(COMPUTER, b1, 3, 1), 3, "Expected result is 3")
# ===================================================

if __name__ == "__main__":
    unittest.main()