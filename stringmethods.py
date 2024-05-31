s1="shrirampurcity"
s2="CDJ RBNB"
s3="102030"
s4="cd jain college"

print(s1.capitalize())

print(s2.casefold())

x=s1.center(30,"*")
print(x)

print(s1.count("r"))

print(s1.encode())

print(s2.find("D"))

print(s1.index("r"))

print(s2.isalnum())

print(s1.isalpha())

print(s3.isdigit())

print(s4.partition("college"))

print(s2.replace("RBNB","College"))


a=input("Enter string:")
if a.endswith("city"):
    print("it is a city")
else:
    print("error")