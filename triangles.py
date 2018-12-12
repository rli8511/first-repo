import math
def square_root(s1,s2):
    return(math.sqrt(s1**2 + s2**2))

s1 = int(input("Please enter the length of one side of the triangle: "))
s2 = int(input("Please enter the length of the second side of the triangle: "))
print(square_root(s1,s2))
