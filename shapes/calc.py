import json
import math
import os
from shapes.detect import Detect
from dotenv import load_dotenv
load_dotenv()


class Calc(object):
    def __init__(self, list_shape):
        """Author: Maor Maharizi,
                Created: 04.02.2023,
                Detail: init calc class
                Return: Null"""
        self.list_shape = Detect(list_shape)

    def rectangle_perimeter(self):
        # calc rectangle perimeter if the shape is rectangle
        try:
            if not self.list_shape.is_rectangle():
                raise ValueError
            else:
                return sum(self.list_shape.list_sides)
        except Exception as e:
            return str(e)

    def rectangle_area(self):
        # calc rectangle area if the shape is rectangle
        # a * b
        try:
            if not self.list_shape.is_rectangle():
                raise ValueError
            else:
                return self.list_shape.list_sides[json.loads(os.getenv("ZERO"))] * self.list_shape.list_sides[json.loads(os.getenv("TWO"))]
        except Exception as e:
            return str(e)

    def triangle_perimeter(self):
        # calc triangle perimeter if the shape is triangle
        try:
            if not self.list_shape.is_triangle():
                raise ValueError
            else:
                return sum(self.list_shape.list_sides)
        except Exception as e:
            return str(e)

    def triangle_area(self):
        # calc triangle area if the shape is triangle
        # s = (a + b + c)/2
        # √[s(s-a)(s-b)(s-c)]
        try:
            if not self.list_shape.is_triangle():
                raise ValueError
            else:
                s = sum(self.list_shape.list_sides) / 2
                res = math.sqrt(s * (s - self.list_shape.list_sides[0]) * (s - self.list_shape.list_sides[1]) * (s - self.list_shape.list_sides[2]))
                return res
        except Exception as e:
            return str(e)

    def square_perimeter(self):
        # calc square perimeter if the shape is square
        try:
            if not self.list_shape.is_square():
                raise ValueError
            else:
                return sum(self.list_shape.list_sides)
        except Exception as e:
            return str(e)

    def square_area(self):
        # calc square perimeter if the shape is square
        # a * a
        try:
            if not self.list_shape.is_square():
                raise ValueError
            else:
                return self.list_shape.list_sides[json.loads(os.getenv("ZERO"))] * self.list_shape.list_sides[json.loads(os.getenv("ONE"))]
        except Exception as e:
            return str(e)
