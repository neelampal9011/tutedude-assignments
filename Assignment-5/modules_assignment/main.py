import math_utils

print("add:", math_utils.add(10, 5))
print("subtract:", math_utils.subtract(10, 5))
print("square:", math_utils.square(4))

from math_utils import square
print("square only:", square(6))


import string_utils
print("capitalize words:", string_utils.capitalize_words("hello world"))
print("reverse string:", string_utils.reverse_string("neelam kumari"))
print("word count:", string_utils.word_count("hello my name is neelam"))


import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

print("discount:", disc.apply_discount(1000, 10))
print("flat discount:", disc.flat_discount(1000))

prices = [100, 200, 300]

total = calculate_total(prices)
print("total:", total)

final_amount = apply_tax(total)
print("final amount:", final_amount)