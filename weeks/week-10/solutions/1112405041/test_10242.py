import unittest
from io import StringIO
import sys
import importlib

problem_10242 = importlib.import_module("10242")

class TestFourthPoint(unittest.TestCase):
    def test_sample(self):
        # 輸入兩個相連的線段 (0,0)-(1,1) 和 (1,1)-(0,1)
        # 共同點是 (1,1)，其他兩點 (0,0), (0,1)
        # 第四點 = (0,0) + (0,1) - (1,1) = (-1, 0)
        input_str = "0.0 0.0 1.0 1.0 1.0 1.0 0.0 1.0"
        expected_output = "-1.000 0.000\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10242.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
