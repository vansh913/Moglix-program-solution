import unittest
from solution import longest_valid_parentheses


class TestLongestValidParentheses(unittest.TestCase):

    def test_given_examples(self):
        #direct from the problem statement  
        self.assertEqual(longest_valid_parentheses("(()"), 2)
        self.assertEqual(longest_valid_parentheses(")()())"), 4)
        self.assertEqual(longest_valid_parentheses(""), 0)

    def test_no_valid_pairs(self):
        #nothing but one types of bracket, so nothing can match
        self.assertEqual(longest_valid_parentheses("((("), 0)
        self.assertEqual(longest_valid_parentheses(")))"), 0)

    def test_fully_valid_string(self):
        self.assertEqual(longest_valid_parentheses("()()"), 4)
        self.assertEqual(longest_valid_parentheses("()()"), 4)

    def test_valid_part_in_middle(self):
        #leading ')' with no match, then a valid part after it
        self.assertEqual(longest_valid_parentheses(")(()"), 2)


if __name__ == "__main__":
    unittest.main()



