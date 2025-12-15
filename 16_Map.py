# # using function
# # def C_to_F(temp):
# #     return (temp * 9/5)+32

celsius_temp = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

# # fahrenheit_temp = list(map(C_to_F, celsius_temp))
fahrenheit_temp = list(map(lambda temp:(temp * 9/5)+32, celsius_temp))

print(fahrenheit_temp)

# sum = lambda x,y,z: x+y+z

# print(sum(1,2,3))

# Easy
roll=[1,2,3,4,5,6,7,8,9,10]

marks=list(map(lambda x:(x+60),roll))

print(marks)