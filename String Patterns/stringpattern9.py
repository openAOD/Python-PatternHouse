print('Enter a string')
pattern_string = input()
print('Enter the number of lines')
lines = int(input())
index = 0
for i in range (lines) :
  for j in range (i+1) :
    try:
       print(pattern_string[index], end=' ')  
       index+= 1
    except:
       print(pattern_string[0], end=' ') 
       index = 1
  print(end='\n')
