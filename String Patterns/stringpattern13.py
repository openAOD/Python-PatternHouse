s = "PatternHouse"
n = 5
s *= (n**2//len(s)+1)
c = 0
for i in range(1, n):
    print(" "*(n-i)+s[c:c+(i*2)-1])
    c += i