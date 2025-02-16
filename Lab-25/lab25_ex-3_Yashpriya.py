# Part-A
# a)
from utils import math_utils
print(f"Sum: {math_utils.add(2, 5)}")
print(f"Difference: {math_utils.subtract(3, 7)}")
print(f"Product: {math_utils.multiply(5, 8)}")
print(f"Quotient: % .2f" % math_utils.divide(4, 7))
print(f"Remainder: {math_utils.get_remainder(7, 5)}")

# b)
import utils.math_utils
print(f"Product (using utils.math_utils): {utils.math_utils.multiply(2, 10)}")

# c)
from utils.math_utils import add
print(f"Total (using utils.math_utils): {add(17, 12)}")
# print(f"Subtraction (using utils.math_utils): {subtract(17, 12)}")   # Will show NameError

# d)
from utils import math_utils as mu
print(f"Difference (using alias): {mu.subtract(29, 24)}")
print(f"Multiplication (using alias): {mu.multiply(29, 24)}")


# Part-B
# a)
from utils import String_utils
print(f"Upper case: {String_utils.convert_upper("hello")}")

# b)
import utils.String_utils
print(f"Lower case: {utils.String_utils.convert_lower("HI")}")

# c)
from utils.String_utils import concatenate
print(f"Concatenated string: {concatenate("Hello", "Yashpriya")}")
# print(convert_upper("hola"))   # NameError

# d)
from utils import String_utils as su
print(f"Lower case (using alias): {su.convert_lower("BDB")}")

