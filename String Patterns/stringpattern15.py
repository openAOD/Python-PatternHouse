s = "ABCDE"
half = round(len(s)/2)
for i in range(len(s)):
    if i == half:
        print(" ".join(s))
    elif i != half:
        print(" "*(half*2)+s[i])