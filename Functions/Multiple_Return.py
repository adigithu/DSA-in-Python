import math
def circle_stats(radius):
    area=round(math.pi*radius**2, 2)
    circumference=round(2*math.pi*radius, 2)
    return area, circumference
num=int(input("Enter the radius in cm: "))
a,c=circle_stats(num)
print(f"The area is {a} and the circumference is {c}")