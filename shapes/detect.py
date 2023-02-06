import json
import os
from dotenv import load_dotenv
load_dotenv()


class Detect(object):
    def __init__(self, list_shape):
        """Author: Maor Maharizi,
                Created: 04.02.2023,
                Detail: init detect class
                Return: Null"""
        self.list_sides = list_shape

    def is_rectangle(self):
        # check if shape numbers > 0 and len(shape) = 4
        if all(i > json.loads(os.getenv("ZERO")) for i in self.list_sides) and len(self.list_sides) == json.loads(os.getenv("FOUR")):
            # check if a + c = b + d
            if self.list_sides[json.loads(os.getenv("ZERO"))] + self.list_sides[json.loads(os.getenv("THREE"))] == self.list_sides[json.loads(os.getenv("ONE"))] + self.list_sides[json.loads(os.getenv("TWO"))]:
                return True
            else:
                return False
        else:
            return False

    def is_square(self):
        # check if shape numbers > 0 and len(shape) = 4
        if all(i > json.loads(os.getenv("ZERO")) for i in self.list_sides) and len(self.list_sides) == json.loads(os.getenv("FOUR")):
            # check if all sides is equals
            if all(x == self.list_sides[json.loads(os.getenv("ZERO"))] for x in self.list_sides):
                return True
            else:
                return False
        else:
            return False

    def is_triangle(self):
        # check if shape numbers > 0 and len(shape) = 3
        if all(i > json.loads(os.getenv("ZERO")) for i in self.list_sides) and len(self.list_sides) == json.loads(os.getenv("THREE")):
            # check if two sides > tree side
            if self.list_sides[json.loads(os.getenv("ZERO"))] + self.list_sides[json.loads(os.getenv("ONE"))] > self.list_sides[json.loads(os.getenv("TWO"))]\
                    and self.list_sides[json.loads(os.getenv("ZERO"))] + self.list_sides[json.loads(os.getenv("TWO"))] > self.list_sides[json.loads(os.getenv("ONE"))] \
                    and self.list_sides[json.loads(os.getenv("ONE"))] + self.list_sides[json.loads(os.getenv("TWO"))] > self.list_sides[json.loads(os.getenv("ZERO"))]:
                return True
            else:
                return False
        else:
            return False
