import json
import os
from shapes.detect import Detect
from shapes.calc import Calc
import dotenv
from shapes.log_manage import LogManage
dotenv.load_dotenv()


class Complex(object):
    def __init__(self, list_of_lists):
        """Author: Maor Maharizi,
                Created: 04.02.2023,
                Detail: init complex class
                Return: Null"""
        self.l = LogManage()
        self.l.open_file()
        self.dict = {}
        self.square = []
        self.triangle = []
        self.rectangle = []
        self.no_shape = []
        self.detect = None
        self.calc = None
        self.list_of_lists = list_of_lists
        self.l.write_to_log(self.list_of_lists)
        self.list_of_lists = sorted(self.list_of_lists, key=lambda x: x[0])
        self.l.write_to_log(self.list_of_lists)
        self.raise_on_error = os.getenv("RAISE_ON_ERROR")

    def check_shape(self):
        # loop of any shape in list of lists
        for i in self.list_of_lists:
            self.detect = Detect(i)
            # case shape is square, calc area and perimeter square and append to square list
            if self.detect.is_square():
                self.calc = Calc(i)
                self.square.append(
                    {os.getenv("SIDES"): i, os.getenv("AREA"): self.calc.square_area(), os.getenv("PERIMETER"): self.calc.square_perimeter()})
            # case shape is rectangle, calc area and perimeter rectangle and append to rectangle list
            elif self.detect.is_rectangle():
                self.calc = Calc(i)
                self.rectangle.append(
                    {os.getenv("SIDES"): i, os.getenv("AREA"): self.calc.rectangle_area(), os.getenv("PERIMETER"): self.calc.rectangle_perimeter()})
            # case shape is triangle, calc area and perimeter triangle and append to triangle list
            elif self.detect.is_triangle():
                self.calc = Calc(i)
                self.triangle.append(
                    {os.getenv("SIDES"): i, os.getenv("AREA"): self.calc.triangle_area(), os.getenv("PERIMETER"): self.calc.triangle_perimeter()})
            # the improper shapes, if raise_on_error raise exception
            else:
                if self.raise_on_error == 'True':
                    raise ValueError
                self.no_shape.append(i)
        # remove double equals items
        [self.square.remove(i) if self.square.count(i) > int(os.getenv("ONE")) else print() for i in self.square]
        [self.rectangle.remove(i) if self.rectangle.count(i) > int(os.getenv("ONE")) else print() for i in self.rectangle]
        [self.triangle.remove(i) if self.triangle.count(i) > int(os.getenv("ONE")) else print() for i in self.triangle]
        [self.no_shape.remove(i) if self.no_shape.count(i) > int(os.getenv("ONE")) else print() for i in self.no_shape]
        # add the Square and Rectangle and Triangle lists to dictionary
        self.dict['Square'] = self.square
        self.dict['Rectangle'] = self.rectangle
        self.dict['Triangle'] = self.triangle
        self.l.write_to_log(self.dict)
        self.l.write_to_log(self.no_shape)
        return True
