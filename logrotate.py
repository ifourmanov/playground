#!/usr/bin/env python
import os.path
import re

filename='/home/ifourmanov/playground/somefile.log'
copies=2


def remove_older(filename, copies):
  reg=os.path.basename(filename)+'.([0-9]+)$'
  for file in os.listdir(os.path.dirname(filename)):
    logfile = re.match(reg, file)
    if logfile and int(logfile.group(1)) >= copies:
      if os.path.isfile(file):
        os.remove(file)
  
def rotate_logs(filename, copies):
  for i in range(copies, 0, -1):
    rotate_log(filename+'.'+str(i), filename+'.'+str(i+1))      
  rotate_log(filename, filename+'.1')



def rotate_log(oldname, newname):
  """Rotates files by writing contents of current log into a rotated one
  """
  if os.path.isfile(oldname):
    with open(newname, 'w') as newfile:
      with open(oldname, 'r') as oldfile:
        newfile.write(oldfile.read())
        oldfile.close()
        with open(oldname, 'w') as oldfile:
          oldfile.write('')
          oldfile.close()
      newfile.close()
      

remove_older(filename, copies)
rotate_logs(filename, copies)
