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
    
    def test_valid_multiple_chunks(self):
        #two separate valid stretches broken by an unmatched ')'
        self.assertEqual(longest_valid_parentheses("()(())"), 6)
        self.assertEqual(longest_valid_parentheses("(()))(()())"), 6)

    def test_nested_inside_unmatched(self):
        #valid nested block sitting after some leading junk
        self.assertEqual(longest_valid_parentheses(")()(((()))"), 6)

if __name__ == "__main__":
    unittest.main()



