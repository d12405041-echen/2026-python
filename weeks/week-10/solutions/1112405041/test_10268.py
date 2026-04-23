import unittest
from io import StringIO
import sys
import importlib

# 由於 10268 涉及多項式，我們用 simple case 測試
# f(x) = 7x^2 + 2x + 1 -> f'(x) = 14x + 2
# f'(3) = 14*3 + 2 = 44
problem_10268 = importlib.import_module("10268")

class TestDerivative(unittest.TestCase):
    def test_sample(self):
        input_str = "3\n7 2 1\n"
        expected_output = "44\n"

        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        sys.stdout = StringIO()
        sys.stdin = StringIO(input_str)

        try:
            problem_10268.solve()
            self.assertEqual(sys.stdout.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

if __name__ == "__main__":
    unittest.main()
