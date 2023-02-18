fo = open('abc.txt', "r+")
print("Name of the file: ", fo.name)
hi = "hello world"
fo.write(hi)
str = fo.readlines()
print("the read string is\n", str)
fo.close()