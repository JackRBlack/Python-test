# define a function to give Fibonacci sequence.

# return the Fibonacci sequence to a list variable
def Fib(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(b)
        a, b = b, a + b
    return result

def Fib2(x):
    a, b = 0, 1
    result = []
    while b <= x:
        result.append(b)
        a, b = b, a + b
    return result

# print the Fibonacci sequence
def pFib(n):
    a, b = 0, 1
    for i in range(n):
        print(b, end = ' ')
        a, b = b, a + b
    print()
    return

def pFib2(x):
    a, b = 0, 1
    while b <= x:
        print(b, end = ' ')
        a, b = b, a + b
    print()
    return

# for running this script in command line
if __name__ == "__main__":
    import sys
    pFib2(int(sys.argv[1]))

