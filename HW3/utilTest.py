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
        self.assertEqual(iter_matrix(HUMAN, b1, 2, 1), 4, "Expected result is 4")
# ===================================================

if __name__ == "__main__":
    unittest.main()