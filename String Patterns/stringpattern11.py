print('Enter a string')
pattern_string = input()
reverse = pattern_string[::-1]
str_length = len(pattern_string)
for i in range (str_length) :
  for j in range (i, str_length-1) :
    print(' ', end =' ')
  for ch in reverse [0:i+1] :
    print(ch, end =' ')
  print(end ='\n') 
