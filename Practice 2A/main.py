import math
# 1. Create a function that computes the area of a triangle using Heron's formula:



def area_of_triangle(a,b,c):
    z = a + b + c
    s = z / 2
    x = math.sqrt(s * ((s - a) * (s - b) * (s - c)))
    return x

A = int(input("Enter side of Triangle: "))
B = int(input("Enter side of Triangle: "))
C = int(input("Enter side of Triangle: "))

result = area_of_triangle(A, B, C)
print(f"The area of the triangle is {result}")

print("\n")

# 2. Create a function that determines whether a given year is a leap year or not.

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

leap = int(input("Please enter year: "))
result = leap_year(leap)
print(f"{leap} As a leap year is {result}")

