import json
import os
import pytest as pytest
from shapes import log_manage
from shapes.detect import Detect
from dotenv import load_dotenv
load_dotenv('C:\\Users\\User\\PycharmProjects\\Shape2\\test\\.env')

l = log_manage.LogManage()
l.open_file()


@pytest.fixture
def detect():
    """Author: Maor Maharizi,
            Created: 04.02.2023,
            Detail: init detect class
            Return: Null"""
    return Detect(json.loads(os.getenv("SHAPE")))


@pytest.mark.test_is_rectangle
def test_is_rectangle(detect):
    # check the shape in .env file
    try:
        assert detect.is_rectangle() == True
        l.write_to_log(os.getenv('IS_RECTANGLE_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('IS_RECTANGLE_TEST') + str(e))


@pytest.mark.test_is_square
def test_is_square(detect):
    # check the shape in .env file
    try:
        assert detect.is_square() == True
        l.write_to_log(os.getenv('IS_SQUARE_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('IS_SQUARE_TEST') + str(e))


@pytest.mark.test_is_triangle
def test_is_triangle(detect):
    # check the shape in .env file
    try:
        assert detect.is_triangle() == True
        l.write_to_log(os.getenv('IS_TRIANGLE_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('IS_TRIANGLE_TEST') + str(e))