def longest_valid_parentheses(s):
  # I am storing indexes on the stack instead of the actual characters.
  # That way , once I find a matching pair , I can just subtract indexes to get the length of that valid stretch.
  # 
  # -1 sits at the bottom as starting point , so even a valid substring right at the start of the string has something to subtract against.
  stack = [-1]
  max_len = 0

  for i, ch in enumerate(s):
    if ch == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
          #this ')' had nothing to match , so it becomes the new base for whatever valid substring comes next
          stack.append(i)
        else:
          max_len = max(max_len, i - stack[-1])
          
  return max_len

if __name__ == "__main__":
    s = input().strip()
    print(longest_valid_parentheses(s))
          
