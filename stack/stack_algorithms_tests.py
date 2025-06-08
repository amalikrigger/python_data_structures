import unittest
from stack_algorithms import is_balanced, reverse_string, evaluate_postfix

class TestStackAlgorithms(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("a"), "a")

    def test_evaluate_postfix_basic(self):
        self.assertEqual(evaluate_postfix(["2", "3", "+", "4", "*"]), 20)
        self.assertEqual(evaluate_postfix(["5", "1", "2", "+", "4", "*", "+", "3", "-"]), 14)
        self.assertEqual(evaluate_postfix(["2", "3", "+"]), 5)
        self.assertEqual(evaluate_postfix(["8", "2", "/"]), 4)

    def test_evaluate_postfix_edge_cases(self):
        self.assertEqual(evaluate_postfix(["3"]), 3)
        with self.assertRaises(IndexError):
            evaluate_postfix(["+"])  # Not enough operands
        with self.assertRaises(IndexError):
            evaluate_postfix(["2", "+"])  # Not enough operands

    def test_is_balanced_valid_cases(self):
        valid_cases = [
            "()", "[]", "{}", "([{}])", "{[()()]}", "(([]))", "{([])}", "",
            "(((((((((())))))))))", "()()()()()()",
            "a + (b * c) - {d / e}", "[a + b] * (c - d)", "[({a + b}) - c]",
            "[\n(\t{ \n}) ]", "()" * 10000
        ]
        for expr in valid_cases:
            with self.subTest(expr=expr):
                self.assertTrue(is_balanced(expr))

    def test_is_balanced_invalid_cases(self):
        invalid_cases = [
            "(]", "[)", "{]", "[({)]}", "(((", "[[[", "{{{", ")))", "}}}", "]]]", "({[)]}",
            ")(", "}[", "]()", "(((((((((()))))))))))", "[a + b * (c - d}",
            "function(x) { return [1, 2, 3];", "{ [ ( ) ]", "{ [ ( ] ) }", "([{}])]", "([{}])}",
            "(" * 10000 + ")" * 9999
        ]
        for expr in invalid_cases:
            with self.subTest(expr=expr):
                self.assertFalse(is_balanced(expr))

if __name__ == '__main__':
    unittest.main()
