import cProfile
import random

# ---- CoPilot ----

# function that finds the longest parenthesis substring in a string
def copilot_longest_parenthesis_substring(s):
    # initialize the longest substring to be an empty string
    longest_substring = ""

    # function to check if the current substring is a valid substring
    def is_valid_substring(substring):
        # initialize the stack to be an empty list
        stack = []
        # iterate through the characters in the substring
        for char in substring:
            # if the character is an opening parenthesis, push it onto the stack
            if char == "(":
                stack.append(char)
            # if the character is a closing parenthesis, pop the stack
            else:
                # if the stack is empty, the substring is not valid
                if len(stack) == 0:
                    return False
                # otherwise, pop the stack
                else:
                    stack.pop()
        # if the stack is empty, the substring is valid
        return len(stack) == 0

    # iterate through the string
    for i in range(len(s)):
        # initialize the current substring to be an empty string
        current_substring = ""
        # iterate through the rest of the string
        for j in range(i, len(s)):
            # add the current character to the current substring
            current_substring += s[j]
            # if the current substring is a valid parenthesis substring
            if is_valid_substring(current_substring):
                # if the current substring is longer than the longest substring
                if len(current_substring) > len(longest_substring):
                    # update the longest substring
                    longest_substring = current_substring

    # return the longest substring
    return longest_substring

# ---- ChatGPT ----

def chatgpt_longest_parenthesis_substring(s):
  # Create an empty stack
  stack = []
  
  # Keep track of the longest parenthesis substring
  longest = ""
  
  # Iterate over the characters in the string
  for c in s:
    # If the character is an opening parenthesis, add it to the stack
    if c == "(":
      stack.append(c)
    # If the character is a closing parenthesis, pop the last opening parenthesis from the stack
    # and update the longest parenthesis substring if necessary
    elif c == ")":
      if stack:
        stack.pop()
        if len(stack) == 0:
          # If the stack is empty, we have found a complete parenthesis substring
          # Update the longest parenthesis substring if necessary
          if len(longest) < (len(s) - s.index(c)):
            longest = s[s.index(c):]
      else:
        # If there are no opening parenthesis in the stack, reset the stack
        stack = []
  
  # Return the longest parenthesis substring
  return longest

if __name__ == "__main__":
    
    # Create a random string with parenthesis
    s = "".join([random.choice(["(", ")"]) for _ in range(5)])

    # print the string
    print(s)

    # Print the output of both functions
    print(copilot_longest_parenthesis_substring(s))
    print(chatgpt_longest_parenthesis_substring(s))

    # Assert both functions return the same result
    assert copilot_longest_parenthesis_substring(s) == chatgpt_longest_parenthesis_substring(s)

    # Profile the two functions
    cProfile.run("copilot_longest_parenthesis_substring(s)")
    cProfile.run("chatgpt_longest_parenthesis_substring(s)")

    # Result:
    # copilot - 221 / 231 testcases passed - Time Limit Exceeded
    # chatgpt - 12 / 231 testcases passed

    # The winner is CoPilot!
