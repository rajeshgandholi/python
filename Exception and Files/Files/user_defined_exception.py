"""
Example of User Defined Exception
In Python programming, pass is a null statement. The difference between a comment and pass statement in Python is that,
while the interpreter ignores a comment entirely, pass is not ignored. But nothing happens when it is executed. It results
into no operation (NOP).
"""
#define Python user-defined exceptions
class Error(Exception):                     #Inheritance
    """Base class for other exceptions"""
    pass
  
class ValueTooSmallError(Error):        #User defined exception
    """Raised when the input value is too small"""
    pass
 
class ValueTooLargeError(Error):        #User defined exception
    """Raised when the input value is too large"""
    pass
 
# our main program
# user guesses a number until he/she gets it right
# you need to guess this number
number = 10
while True:
    try:
        i_num = int(input("Enter a number: "))   # 8  15   12
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()
    else:
        print("Congratulations! You guessed it correctly.")
        break
