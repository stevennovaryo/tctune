import os
from decouple import config

CURRENT_DIRECTORY = os.getcwd()
TESTCASES_DIRECTORY = os.getcwd() + '\\' + config('TESTCASES_DIRECTORY')
TEMPORARY_DIRECTORY = os.getcwd() + '\\temp'
SLUG = config('SLUG')