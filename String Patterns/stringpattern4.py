print('Enter a string')
pattern_string = input()
str_length = len(pattern_string)
for i in range (str_length) :
  for ch in pattern_string [0:str_length-i] :
    print(ch, end =' ')
  print(end ='\n')  
