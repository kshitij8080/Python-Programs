s = input("Enter String:")
a = {}
for i in range(len(s)):
    if s[i] in s[i+1:]:
        if s[i] in a:
            a[s[i]] += 1
        else:
            a[s[i]] = 2
print(a)
