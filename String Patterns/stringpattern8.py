print('Enter a string')
pattern_string = input() [::-1]
l1=[]
l1.append(pattern_string[4:8])
l1.append(pattern_string[8:])
l1.append(pattern_string[0:4])
for i in range (3):
  for j in range (4):
    print(l1[i][j], end=' ')
  print(end ='\n')  
