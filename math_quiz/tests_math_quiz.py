import unittest
from math_quiz import function_random_number, function_random_operators, function_final


class TestMathGame(unittest.TestCase):
    def test_function_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_random_operators(self):
        valid_operators = {'+', '-', '*', '/'}
        for _ in range(1000):
            rand_operator = function_random_operators()
            self.assertIn(rand_operator, valid_operators)

    def test_function_final(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
        ]
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_final(num1, num2, operator)
            print(problem, answer)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
