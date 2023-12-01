def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

class RationalNumber:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        if denominator != 0:
            self.__denominator = denominator
        else:
            raise ValueError("Denominator should not be 0")

    def __add__(self, other):
        denominator = self.__denominator * other.__denominator
        numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        gcd_value = greatest_common_divisor(numerator, denominator)
        numerator //= gcd_value
        denominator //= gcd_value
        result = RationalNumber(numerator, denominator)
        return result

    def __sub__(self, other):
        denominator = self.__denominator * other.__denominator
        numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        gcd_value = greatest_common_divisor(numerator, denominator)
        numerator //= gcd_value
        denominator //= gcd_value
        result = RationalNumber(numerator, denominator)
        return result

    def __mul__(self, other):
        denominator = self.__denominator * other.__denominator
        numerator = self.__numerator * other.__numerator
        gcd_value = greatest_common_divisor(numerator, denominator)
        numerator //= gcd_value
        denominator //= gcd_value
        result = RationalNumber(numerator, denominator)
        return result

    def __truediv__(self, other):
        numerator = self.__numerator * other.__denominator
        denominator = self.__denominator * other.__numerator
        gcd_value = greatest_common_divisor(numerator, denominator)
        numerator //= gcd_value
        denominator //= gcd_value
        result = RationalNumber(numerator, denominator)
        return result

    def __eq__(self, other):
        return self.__numerator * other.__denominator == other.__numerator * self.__denominator

    def to_float(self):
        return self.__numerator / self.__denominator

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

rational_number1 = RationalNumber(1, 2)
rational_number2 = RationalNumber(3, 4)

result_addition = rational_number1 + rational_number2
print(f"Addition: {rational_number1} + {rational_number2} = {result_addition}")

result_subtraction = rational_number1 - rational_number2
print(f"Subtraction: {rational_number1} - {rational_number2} = {result_subtraction}")

result_multiplication = rational_number1 * rational_number2
print(f"Multiplication: {rational_number1} * {rational_number2} = {result_multiplication}")

result_division = rational_number1 / rational_number2
print(f"Division: {rational_number1} / {rational_number2} = {result_division}")

equality_check = rational_number1 == RationalNumber(2, 4)
print(f"Equality check: {rational_number1} == {RationalNumber(2, 4)} is {equality_check}")

float_value = rational_number1.to_float()
print(f"Float value of {rational_number1}: {float_value}")
