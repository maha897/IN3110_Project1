"""
Tests for our array class
"""

from array_class import Array
import pytest

# 1D tests (Task 4)

array1 = Array((6,), 1, 2, 3, 4, 5, 6)
array2 = Array((6,), 2, 4, 6, 1, 3, 5)
array3 = Array((6,), 1, 0, 3, 0, 5, 0)
array4 = Array((4,), True, True, False, False)
array5 = Array((5,), 1, 1, 1, 1, 1)

# Expected output for test_same_1d()
e_boolarr1 = [False, False, False, False, False, False]
e_boolarr2 = [True, False, True, False, True, False]
e_boolarr3 = [False, True, False, True, False, True]

# Content of __str__ from Array class
def test_str_1d():
    assert array1.__str__() == "[1, 2, 3, 4, 5, 6]"

@pytest.mark.parametrize("arg1, arg2, e", [
    (array1, array2, [3, 6, 9, 5, 8, 11]),
    (array1,  1, [2, 3, 4, 5, 6, 7]),
    (3, array2, [5, 7, 9, 4, 6, 8]),
    (array1, array5, IndexError),
    (array1, array4, TypeError),
    (array4, 5, ValueError),
    (array1, 'hello', ValueError)])

# Content of __add__/__radd__ from Array class
def test_add_1d(arg1, arg2, e):
    if type(e) == type and issubclass(e, Exception):
        with pytest.raises(e):
            arg1+arg2 
    else:
        assert arg1+arg2 == e


@pytest.mark.parametrize("arg1, arg2, e", [
    (array1, array2, [-1,-2,-3,3,2,1]),
    (array1,  5, [-4,-3,-2,-1,0,1]),
    (3, array2, [1,-1,-3,2,0,-2]), 
    (array1, array5, IndexError),
    (array1, array4, TypeError),
    (array4, 5, ValueError),
    (array1, 'hello', ValueError)]) 

# Content of __sub__/__rsub__ from Array class
def test_sub_1d(arg1, arg2, e):
    if type(e) == type and issubclass(e, Exception):
        with pytest.raises(e):
            arg1-arg2 
    else:
        assert arg1-arg2 == e


@pytest.mark.parametrize("arg1, arg2, e", [
    (array1, array2, [2,8,18,4,15,30]),
    (array1,  2, [2,4,6,8,10,12]),
    (3, array2, [6,12,18,3,9,15]),
    (array1, array5, IndexError),
    (array1, array4, TypeError),
    (array4, 5, ValueError),
    (array1, 'hello', ValueError)])

# Content of __mul__/__rmul__ from Array class
def test_mul_1d(arg1, arg2, e):
    if type(e) == type and issubclass(e, Exception):
        with pytest.raises(e):
            arg1*arg2 
    else:
        assert arg1*arg2 == e


@pytest.mark.parametrize("arr1, arr2, ebool", [
    (array1, array2, False),
    (array1,  array1, True),
    (5, array2, False)])

# Content of __eq__ from Array class
def test_eq_1d(arr1, arr2, ebool):
    assert (arr1== arr2) == ebool


@pytest.mark.parametrize("arg1, arg2, boolarr", [
    (array1, array2, e_boolarr1),
    (array1,  array3, e_boolarr2),
    (array3, 0, e_boolarr3),
    (array1, array5, ValueError)])

# Content of is_equal from Array class
def test_same_1d(arg1, arg2, boolarr):
    if type(boolarr) == type and issubclass(boolarr, Exception):
        with pytest.raises(boolarr):
            arg1.is_equal(arg2)
    else:
        assert arg1.is_equal(arg2) == boolarr


@pytest.mark.parametrize("arr, e", [
    (array1, 1),
    (array4, TypeError)])

# Content of min_element from Array class
def test_smallest_1d(arr, e):
    if type(e) == type and issubclass(e, Exception):
        with pytest.raises(e):
            arr.min_element()
    else:
        assert arr.min_element() == e


@pytest.mark.parametrize("arr, e", [
    (array2, 3.5),
    (array4, TypeError)])

# Content of mean_element from Array class
def test_mean_1d(arr, e):
    if type(e) == type and issubclass(e, Exception):
        with pytest.raises(e):
            arr.mean_element()
    else:
        assert arr.mean_element() == e

# 2D tests (Task 6)

array6 = Array((4,2), 1,2,3,4,5,6,7,8)
array7 = Array((4,2), 1,1,1,1,1,1,1,1)

# Expected output for test_same_2d
e_boolarr4 = [[True, False, False, False],[False, False, False, False]]
e_boolarr5 = [[False, True, False, False],[False, False, False, False]]


@pytest.mark.parametrize("arg1, arg2, e", [
    (array6, array7, [[2,3,4,5],[6,7,8,9]]),
    (array7, 2, [[3,3,3,3],[3,3,3,3]])])

# Content of __add__/__radd__ for 2D arrays
def test_add_2d(arg1, arg2, e):
    assert arg1+arg2 == e


@pytest.mark.parametrize("arg1, arg2, e", [
    (array6, array7, array6),
    (array7, 2, [[2,2,2,2],[2,2,2,2]])])

def test_mult_2d(arg1, arg2, e):
    assert arg1*arg2 == e


@pytest.mark.parametrize("arg1, arg2, boolarr", [
    (array6, array7, e_boolarr4),
    (array6, 2, e_boolarr5)])

def test_same_2d(arg1, arg2, boolarr):
    assert arg1.is_equal(arg2) == boolarr


@pytest.mark.parametrize("arr, e", [
    (array6, 4.5),
    (array7, 1)])

def test_mean_2d(arr, e):
    assert arr.mean_element() == e

if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
    