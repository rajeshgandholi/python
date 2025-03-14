# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    import sys
    input = sys.argv[1]
    fib(int(input))
    # re = fib2(int(input))
    # print(re)

# surname = 'gandholi'


# __all__ = ['fib2']

# from   import sound.effects.echo

# a = sound.effects.echo

# a.echofilter()