import json
import os
import pytest as pytest
from shapes import log_manage
from shapes.calc import Calc
from shapes.detect import Detect
from dotenv import load_dotenv
load_dotenv('C:\\Users\\User\\PycharmProjects\\Shape2\\test\\.env')

l = log_manage.LogManage()
l.open_file()


@pytest.fixture
def calc():
    """Author: Maor Maharizi,
            Created: 04.02.2023,
            Detail: init calc class
            Return: Null"""
    return Calc(json.loads(os.getenv("SHAPE")))


@pytest.mark.rectangle_perimeter
def test_rectangle_perimeter(calc):
    # calc rectangle perimeter if the shape is rectangle
    try:
        assert calc.rectangle_perimeter() == json.loads(os.getenv('RES_PER'))
        l.write_to_log(os.getenv('RECTANGLE_PER_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('RECTANGLE_PER_TEST') + str(e))


@pytest.mark.rectangle_area
def test_rectangle_area(calc):
    # calc rectangle area if the shape is rectangle
    try:
        assert calc.rectangle_area() == json.loads(os.getenv('RES_AREA'))
        l.write_to_log(os.getenv('RECTANGLE_AREA_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('RECTANGLE_AREA_TEST') + str(e))


@pytest.mark.triangle_perimeter
def test_triangle_perimeter(calc):
    # calc triangle perimeter if the shape is triangle
    try:
        assert calc.triangle_perimeter() == json.loads(os.getenv('REZ_PER'))
        l.write_to_log(os.getenv('TRIANGLE_PER_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('TRIANGLE_PER_TEST') + str(e))


@pytest.mark.triangle_area
def test_triangle_area(calc):
    # calc triangle area if the shape is triangle
    try:
        assert calc.rectangle_area() == json.loads(os.getenv('RES_AREA'))
        l.write_to_log(os.getenv('TRIANGLE_AREA_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('TRIANGLE_AREA_TEST') + str(e))


@pytest.mark.square_perimeter
def test_square_perimeter(calc):
    # calc square perimeter if the shape is square
    try:
        assert calc.square_perimeter() == json.loads(os.getenv('RES_PER'))
        l.write_to_log(os.getenv('SQUARE_PER_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('SQUARE_PER_TEST') + str(e))


@pytest.mark.square_area
def test_square_area(calc):
    # calc square perimeter if the shape is square
    try:
        assert calc.square_area() == json.loads(os.getenv('RES_AREA'))
        l.write_to_log(os.getenv('SQUARE_AREA_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('SQUARE_AREA_TEST') + str(e))