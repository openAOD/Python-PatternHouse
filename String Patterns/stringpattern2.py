print('Enter a string')
pattern_string = input()
print('Enter the number of lines')
lines = int(input())
for i in range(lines) :
  for ch in pattern_string [::-1] :
    print(ch, end =' ')
  print(end ='\n')  
