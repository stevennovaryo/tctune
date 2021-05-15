"""
  Use this function to identify if it's an input file by it's name
"""
def check_input_file(file_name):
  if file_name[-3:] == '.in':
    return True
  return False


"""
  Use this function to get the name of output file from input file's name
"""
def get_output_file_name(input_file_name):
  return input_file_name[:-3] + '.out'