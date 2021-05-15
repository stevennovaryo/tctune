from user_modified.input_format import input_format
import user_modified.subtasks
import user_modified.sample_testcases

class SubtaskChecker:
  subtask = {}
  subtask_count = {}

  sample_testcases = {}
  sample_OK = {}


  def add_subtask(self, subtask_name):
    subtask_id = int(subtask_name[7:])
    self.subtask[subtask_id] = getattr(user_modified.subtasks, subtask_name)
    self.subtask_count[subtask_id] = 0
    
    print(f'subtask {subtask_id} added')


  def add_sample_testcase(self, sample_name):
    sample_id = int(sample_name[6:])
    sample_content = '\n'.join(getattr(user_modified.sample_testcases, sample_name))
    self.sample_testcases[sample_id] = sample_content
    self.sample_OK[sample_id] = False

    print(f'sample {sample_id} added')
    print(sample_content)


  def __init__(self):
    for attr_name in dir(user_modified.sample_testcases):
      if (attr_name[0:6] != 'sample'):
        continue
      self.add_sample_testcase(attr_name)
    
    for attr_name in dir(user_modified.subtasks):
      if (attr_name[0:7] != 'subtask'):
        continue
      self.add_subtask(attr_name)
      

  def check_sample(self, input_file):
    input_content = input_file.read()
    input_content = input_content.replace('\n', ' ').split(' ')

    for sample_id, sample_content in self.sample_testcases.items():
      sample_content = sample_content.replace('\n', ' ').split(' ')
      if (sample_content != input_content):
        continue
        
      self.sample_OK[sample_id] = True
      return 'sample', sample_id
    
    return None


  def check_subtask(self, input_file, output_file):
    input_kwargs = input_format(input_file)
    result = 420691273

    for subtask_id, checker in self.subtask.items():
      if checker(**input_kwargs):
        result = min(result, subtask_id)
  
    self.subtask_count[result] += 1
    return result, self.subtask_count[result]
  

  def check(self, input_file_path, output_file_path):
    input_file = open(input_file_path, 'r')
    output_file = open(output_file_path, 'r')

    sample_name = self.check_sample(input_file)
    if sample_name:
      return sample_name
    
    input_file.seek(0)
    return self.check_subtask(input_file, output_file)

  def finalize(self):
    for sample_id, ok in self.sample_OK.items():
      if ok == True:
        continue
      print(f'[ERROR] sample {sample_id} is missing')


subtask_checker = SubtaskChecker()