# Longest Valid Parentheses

This is my solution of the " Longest Valid Parentheses " problem - given a string of just '(' and ')', find the lobgest substring that's actually a valid, well fomed sequence.

### Example

Input:")()())"
Output:4#"()()"

## My Approach

The brute-force technique would be checking evry substring, that is O(n³) and too slow given that the string can be upto 30,000 characters long. So, I went with the Stack-Based Technique instead of O(n) and once it clicks its is pretty clean.

Instead of pushing the actual  `(` and `)` characters, I push their 'indices'. In that way when I find a matching pair , I can just subtarct indices to get the length of that valid stretch.

I start the stack with `-1` at the bootom as a base marker - that way even a valid substring right at the start of the string has something to subtract against, no extra edge case needed.

Then scanning through the string:
- On `(`, push its index.
- On `)`, pop the top of the stack.
  - If that empties the stack, this ')' had nothing to match, so it becomes the new base - pus its index instead.
  - If the stack is not empty after popping, I have just closed a valid pair.
    The length of the valid rin is 'i - stack[-1]'

Every time I get a valid length, I check it against the max seen so far.

Complexity: O(n) time, O(n) space (worst case is tring of all '(', where every index ends on the stack. 

## Run

```bash
python solution.py
```

(reads a line of input and print the answer)

## TEST

```bash
python -m unittest test_solution.py -v
```

ALL test cse pass locally 
