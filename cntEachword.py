s1 = input("Enter String:")
a = {}
for ch in s1:
    if ch in a:
        a[ch] = a[ch]+1
    else:
        a[ch] = 1

print(a)
