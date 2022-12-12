# Find the next even number

def find_next_even(num):
  # If the number is even, add 2 to get the next even number
  if num % 2 == 0:
    return num + 2
  # If the number is odd, add 1 to get the next even number
  else:
    return num + 1

# Test the function
print(find_next_even(5))  # should print 6
print(find_next_even(12))  # should print 14