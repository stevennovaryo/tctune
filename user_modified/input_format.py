"""
  Use this function to read input and format it to a certain variables that can be used and return it as kwargs.
  The example as follow read input as:
  N M
  A_1 A_2 ... A_N 
"""
def input_format(input_file):
  N, M = input_file.readline().split()
  N, M = map(int, (N, M))

  A = input_file.readline().split()
  A = list(map(int, A))
  
  result = {'N': N, 'M': M, 'A': A}
  return result