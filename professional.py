""" Here I define how a professional do this program."""
# let's first define class
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_into_rectangle(self,rectangle):
        if rectangle.lower_left.x < self.x < rectangle.upper_right.x and rectangle.lower_left.y < self.y < rectangle.upper_right.y:
            print("Point is inside the rectangle.")
        else :
            print("Point is outside the rectangle.")

    def far_from(self,point):
        return ((point.x - self.x)**2 + (point.y - self.y)**2)**0.5

class Rectangle:

    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right

# let's make lower_left and upper_right by random generator
from random import randint

lower_left = Point(randint(0, 99), randint(0, 99))
upper_right = Point(randint(lower_left.x + 1, 100), randint(lower_left.y + 1, 100))

# let's make rectangle by rectangle class
rectangle = Rectangle(lower_left, upper_right)
print(f"Lower_left Point : {(rectangle.lower_left.x, rectangle.lower_left.y)}\nUpper_right Point : {(rectangle.upper_right.x, rectangle.upper_right.y)}")

# let's take input from user and make it a point
try:  # this try function if we input any kind of string in input section then It will not show any error.
    user_point = Point(float(input('Input the x cordinate of your guessing point: ')), float(input('Input the y cordinate of your guessing point: ')))
    user_point.falls_into_rectangle(rectangle)
except:
    print('Please enter numbers not string.')

# In this method of programming you can add any function Like in Point class  we added  far_from for two point distance
# like this we can also add area Function in Rectangle  class.