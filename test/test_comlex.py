import json
import os
import pytest as pytest
from shapes import log_manage
from shapes.complex import Complex
from dotenv import load_dotenv
load_dotenv('C:\\Users\\User\\PycharmProjects\\Shape2\\test\\.env')

l = log_manage.LogManage()
l.open_file()


@pytest.fixture
def comp():
    """Author: Maor Maharizi,
            Created: 04.02.2023,
            Detail: init complex class
            Return: Null"""
    return Complex(json.loads(os.getenv("LIST_OF_LISTS_TEST")))


@pytest.mark.check_shape
def test_check_shape(comp):
    # check all shapes in list
    try:
        assert comp.check_shape() == True
        l.write_to_log(os.getenv('CHECK_SHAPE_TEST') + os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('CHECK_SHAPE_TEST') + str(e))