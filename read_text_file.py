# a program for reading file or images or documents

import os

path = './textfiles/'                 # enter the path to the text file
dir_list = os.listdir(path)

# print(f'files in the folder {path} are {dir_list}')

for i in range(0, len(dir_list)):
  file_name = dir_list[i]
  file_path = [path+dir_list[i]]

  with open(file_path[0], 'r') as file: # file_path[0] to read the first file as for loop is changing the index
    # print(f'{file_path[0]}')  
    for _ in range(100):                # no. of times the for loop is executed is supposed
      data = file.readline().rstrip()   # rstrip() is used to avoid spaces in the text
      if not data:
          break
      # print(data)
      data = data.replace(" ","")
      print(data)