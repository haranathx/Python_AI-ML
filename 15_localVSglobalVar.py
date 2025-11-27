x = 4
print(x)
print("")

def hello():
    global x
    x = 5
    print(f"local variable of x is {x}")
    print("Hello GGG")



hello()
print(f"The global x is {x}")
print("")
print(f"The global x is {x}")
