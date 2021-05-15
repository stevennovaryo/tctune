"""
  This file contains all subtasks.
  All function in this file should start with prefix "subtask" and followed by the id of subtask (integer).
"""

def subtask1(**kwargs):
  N, M, A = kwargs['N'], kwargs['M'], kwargs['A']

  ok = True
  ok &= (1 <= N <= 10)
  ok &= (1 <= M <= 10)
  
  return ok

def subtask2(**kwargs):
  N, M, A = kwargs['N'], kwargs['M'], kwargs['A']

  ok = True
  ok &= (1 <= N <= 1000)
  ok &= (1 <= M <= 1000)
  
  return ok

def subtask3(**kwargs):
  return True