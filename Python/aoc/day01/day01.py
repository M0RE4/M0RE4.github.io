def solutionA(numbers):
  # TODO: replace with code solving the problem
  result = -1 # Dummy result
  return result


def solutionB(numbers):
  # TODO: replace with code solving the problem
  result = -1 # Dummy result
  return result


# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines


if __name__ == "__main__":
  input_file_name = "dummy-input.txt"
  # TODO: Uncomment line below to use real input
  input_file_name = "dummy-input.txt" 
  
  print(f"Loading data from: {input_file_name}")
  lines = load_data(input_file_name)
  
  # converts lines to numbers (depends on the task)
  numbers = [int(i) for i in lines]

  resultA = solutionA(numbers)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(numbers)
  print(f"Solution for part B: {resultB}")