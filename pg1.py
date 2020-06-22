#! /usr/bin/python
import errno
import os
import shutil 
from os import makedirs
#from distutils.dir_util import copy_tree

def main():

  try:
    for i in range(1,101):
        os.mkdir(r'C:\Users\LENOVO\Desktop\assignment2\%s' % i) 
        print("Directory created")
          
  except FileExistsError:
        print("Folders are already exists")
        src = r'C:\Users\LENOVO\Desktop\assignment2'
        dest = r'C:\Users\LENOVO\Desktop\as1'
 #       head_tail = os.path.split(src) 
        list=['1','2','4','22','11']
        arr=os.listdir(src)
        #print(cmp(list,arr))
#        print(type(arr))
#        print(type(list))
#        print(head_tail)
    
        for j in list:
           shutil.copytree(os.path.join(src,j), os.path.join(dest,j),ignore = ignore_pyc_files) 
           print(j)
#        fromDirectory = r'C:\Users\LENOVO\Desktop\assignment2\1\2\3\4'
#        toDirectory = r'C:\Users\LENOVO\Desktop\m\1\2\3'
#            copy_tree(fromDirectory, toDirectory)
 #      for list in src:
  #       shutil.copytree(src,dest)
        
        

        
        
if __name__=='__main__':
    main()
    
    