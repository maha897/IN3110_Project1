"""
Array class for assignment 2
"""

from typing import List, Tuple, Union
from math import prod

class Array:

    def __init__(self, shape : Tuple, *values) -> None:
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        if self.__check_init(shape, values):

            one_dim_arr = list(values)

            if len(shape) == 2: # For two dimensional arrays
                array = [one_dim_arr[i:i+shape[0]] for i in range(0, len(one_dim_arr), shape[0])]

            elif len(shape) == 1: # For one dimensional arrays
                array = one_dim_arr 
            
            else: #  Not implemented for n-dimensional arrays for now
                NotImplemented

            self.array = array
            self.one_dim_arr = one_dim_arr
            self.shape = shape
            self.first = one_dim_arr[0]

            # For two dimensional arrays
            self.columns = shape[0]
            try:
                self.rows = shape[1]
            except IndexError:
                self.rows = 1

    def __getitem__(self, i : int) -> Union[int,list]: 
        """Returns array element of index.

        Input:
            i: int, the index of desired element.

        Output:
            either an int, float or bool, depending on what datatypes the array consists of. Can also return a list.

        """

        return self.array[i]

    def __str__(self) -> str:
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """

        return str(self.array)

    def __add__(self, other) -> "Array":
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """

        if isinstance(self.first, bool):
            raise ValueError("Undefined operation for type bool.")

        elif isinstance(other, (int, float)):
            added_arr = [elem + other for elem in self.one_dim_arr]

        elif isinstance(other, Array):

            if type(self.first) != type(other.first):
                raise  TypeError("Arrays must contain elements of same type.")
            elif self.shape != other.shape:
                raise IndexError(f"Shapes must be the same. {self.shape} != {other.shape}")
            
            else:
                added_arr = [elem_self + elem_other for elem_self, elem_other in zip(self.one_dim_arr, other.one_dim_arr)]

        else:
            raise ValueError("Unsupported value for operation.")

        return Array(self.shape, *added_arr)

    def __radd__(self, other) -> "Array":
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other) -> "Array":
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
    
        if isinstance(self.first, bool):
            raise ValueError("Undefined operation for type bool.")

        elif isinstance(other, (int, float)):
            subbed_arr = [elem - other for elem in self.one_dim_arr]

        elif isinstance(other, Array):

            if type(self.first) != type(other.first):
                raise  TypeError("Arrays must contain elements of same type.")
            elif self.shape != other.shape:
                raise IndexError(f"Shapes must be the same. {self.shape} != {other.shape}")
            
            else:
                subbed_arr = [elem_self - elem_other for elem_self, elem_other in zip(self.one_dim_arr, other.one_dim_arr)]
            
        else:
            raise ValueError("Unsupported value for operation.")

        return Array(self.shape, *subbed_arr)

    def __rsub__(self, other) -> "Array":
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """

        # I thought it was worth mentioning that i did the rsub method differently
        # than radd and rmul because subtraction is not commutative, 
        # so it made more sense for me personally to do it this way.
        # Due this implementation 3 - array would give [3-array_elem1, 3-array_elem2, ...],
        # and not [array_elem1-3, array_elem2-3, ...].

        if isinstance(other, (int, float)):
            values = [other for i in range(self.columns*self.rows)]
            l_other = Array(self.shape, *values)

        else: 
            raise ValueError("Unsupported value for operation.")

        return l_other.__sub__(self)

    def __mul__(self, other) -> "Array":
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """

        if isinstance(self.first, bool):
            raise ValueError("Undefined operation for type bool.")

        elif isinstance(other, (int, float)):
            mul_arr = [elem*other for elem in self.one_dim_arr]

        elif isinstance(other, Array):

            if type(self.first) != type(other.first):
                raise  TypeError("Arrays must contain elements of same type.")
            elif self.shape != other.shape:
                raise IndexError(f"Shapes must be the same. {self.shape} != {other.shape}")
            
            else:
                mul_arr = [elem_self*elem_other for elem_self, elem_other in zip(self.one_dim_arr, other.one_dim_arr)]
        
        else:
            raise ValueError("Unsupported value for operation.")
     
        return Array(self.shape, *mul_arr)

    def __rmul__(self, other) -> "Array":
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """

        return self.__mul__(other)

    def __eq__(self, other) -> bool:
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If 'other' is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """

        return other == self.array

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If 'other' is an array and the two array shapes do not match, this method should raise ValueError.
        If 'other' is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """

        if isinstance(other, (int, float)):
            bool_arr = [elem == other for elem in self.one_dim_arr]

        elif isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError(f"Arrays need to match in shape. {self.shape} != {other.shape}.")

            else:
                bool_arr = [elem_self == elem_other for elem_self, elem_other in zip(self.one_dim_arr, other.one_dim_arr)]

        if self.rows > 1:
            bool_arr = [bool_arr[i:i+self.columns] for i in range(0, len(bool_arr), self.columns)]
      
        return bool_arr   
      
    def min_element(self) -> Union[int, float]:
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """

        if isinstance(self.first, bool):
            raise TypeError("Unsupported type for finding minimum.")

        return min(self.one_dim_arr)

    def mean_element(self) -> Union[int, float]:
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """

        if isinstance(self.first, bool):
            raise TypeError("Unsupported type for finding mean.")

        return sum(self.one_dim_arr)/len(self.one_dim_arr)

    def __check_init(self, shape : Tuple, values: Tuple) -> bool:
        """
        A helping funcion used for checking conditions of input values in constructor.
        Not for public use.

        Input:
            shape
            values
        
        Output:
            a bool, True if conditions apply, else raises exceptions
        
        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        if not isinstance(shape, tuple):
            raise TypeError("Wrong type for shape. See __doc__ for input types.")

        for value in values:
            if not isinstance(value, (int, float, bool)):
                raise TypeError("Wrong type for values. See __doc__ for input types.")

        for dim in shape:
            if not isinstance(dim, int):
                raise ValueError("Values of shape need to be integers.")

        if not self.__homogenous_type(list(values)):
            raise ValueError("Elements need to all be of same type.")

        values_counted = len(values)
        values_expected = prod(shape)

        if values_expected != values_counted: 
            raise ValueError(f"Shape and number of values need to correspond. Number of values is {values_counted}, shape suggests {values_expected}.")
    
        return True

    def __homogenous_type(self, array : List) -> bool:
        """
        A helping funcion used for checking if all input values are of same type.
        Not for public use.

        Input:
            a list of the initial arguments given when initializing array.
        
        Output:
            a bool, True if all elements are of same type, else False.
        
        """

        return True if all((type(x) is type(array[0])) for x in array) else False
