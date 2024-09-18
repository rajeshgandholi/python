"""create a program where we can raise an exception"""


# # type 1 --> handling error with try/except
# def remainder_division(a, b):
#     result = a//b
#     remainder = a % b
#     print(a, '/', b, 'is', result, 'remainder', remainder)


# #  Main program
# remainder_division(2, 3)
# try:
#     remainder_division(2, 0)
# except Exception:
#     print('Input parameters are not valid!!')


# # type 2 --> handling error by raising the exception

# def remainder_division(a, b):
#     if b == 0:
#         raise ZeroDivisionError
#     result = a//b
#     remainder = a % b
#     print(a, '/', b, 'is', result, 'remainder', remainder)


# #  Main program
# remainder_division(2, 3)
# remainder_division(2, 0)


# type 3 --> handling error by raising the exception along with error message
def remainder_division(a, b):
    if b == 0:
        raise Exception('Divisor cannot be 0')
    result = a//b
    remainder = a % b
    print(a, '/', b, 'is', result, 'remainder', remainder)


#  Main program
remainder_division(2, 3)
remainder_division(2, 0)
