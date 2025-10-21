try:
    L=[1,5,6,7]
    i=int(input("Enter the index : "))
    print(L[i])

except:
    print("Some error occurred")

finally:
    print("I am always executed")