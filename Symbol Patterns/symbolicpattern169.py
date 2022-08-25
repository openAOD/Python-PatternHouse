n=max=5
symbol_arr=[4,3,5,1,2]
for i in range(max):
    for j in range(n):
        if symbol_arr[j] >= max-i:
            print(' # ',end='')
        else:
            print('   ', end='')
    print(end='\n')
for i in range(n):
    print([i+1],end='')


# #include <stdio.h>

# int main()
# {
#     int n = 5, max = 5;
#     int a[] = {4, 3, 5, 1, 2};
#     for(int i = 0; i < max; i++) {
#         for(int j = 0; j < n; j++) {
#             if(a[j] >= max - i)
#                 printf(" # ");
#             else
#                 printf("   ");
#         }
#         printf("\n");
#     }
#     for(int i = 0; i < n; i++)
#         printf("[%d]", i + 1);
#     return 0;
# }
         