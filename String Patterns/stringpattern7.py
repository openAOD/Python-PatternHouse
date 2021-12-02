import math 
print('Enter a string')
pattern_string = input()
print('Enter the number of letters to be printed in each line')
num = int(input())
index = 0
for i in range (math.ceil(len(pattern_string)/num)) :
  for j in range (num):
    try:
      print(pattern_string[index], end=' ')
      index+= 1
    except:
      print(' ', end ='')  
  print(end ='\n')
