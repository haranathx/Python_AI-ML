# n = input("Enter the number : ")
# print(f"Multiplication table of n {n} is : ")

# try:
#     for i in range(1,11):
#         print(f"{int(n)} X {i} = {int (n)*i}")
# except Exception as e:
#     print(e)

# print("Some important lines of code")
# print("End of program")

# we can do this like

n = input("Enter the number : ")
print(f"Multiplication table of n {n} is : ")

try:
    for i in range(1,11):
        print(f"{int(n)} X {i} = {int (n)*i}")
except :
    print("Invalid input !")

print("Some important lines of code")
print("End of program")


# Another one

try:
    num = int(input("Enter a Integer : "))
    a = [6,3]
    print(a[num])

except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index Error.")