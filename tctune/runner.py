import os
import shutil

from tctune.constants import TESTCASES_DIRECTORY, TEMPORARY_DIRECTORY, SLUG
from user_modified.file_name_format import check_input_file, get_output_file_name
from tctune.subtask_checker import subtask_checker

class Runner:
  def rename(self, file_name):
    input_file_name = file_name
    output_file_name = get_output_file_name(input_file_name)

    input_file_path = TESTCASES_DIRECTORY + "\\" + input_file_name
    output_file_path = TESTCASES_DIRECTORY + "\\" + output_file_name

    subtask, subtask_count = subtask_checker.check(input_file_path, output_file_path)

    shutil.copy2(input_file_path, TEMPORARY_DIRECTORY + f'\\{SLUG}_{subtask}_{subtask_count}.in')
    shutil.copy2(output_file_path, TEMPORARY_DIRECTORY + f'\\{SLUG}_{subtask}_{subtask_count}.out')

  def run(self):
    os.mkdir(TEMPORARY_DIRECTORY)

    for file_name in os.listdir(TESTCASES_DIRECTORY):
      if check_input_file(file_name):
        self.rename(file_name)
    
    subtask_checker.finalize()

    shutil.make_archive('tc', 'zip', TEMPORARY_DIRECTORY)
    shutil.rmtree(TEMPORARY_DIRECTORY)

tctune = Runner()