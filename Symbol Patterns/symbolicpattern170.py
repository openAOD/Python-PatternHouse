symbol_list=[4,3,5,1,2]
for i in range(5):
	print([i+1], end='')
	for j in range(symbol_list[i]):
		print('#', end=' ')
	print(end='\n')