# Creating a file
# with open('myfile.txt', 'w') as f:
#     f.write('Hello, World!')

f = open('myfile.txt', 'r')
# print(f)

text = f.read()
print(text)
f.close()