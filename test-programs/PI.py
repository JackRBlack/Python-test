# print PI to n places after the decimal
# doesn't work very well. need improvement.  ---- 2017/09/07

def PI(n):
    from math import pi
    string = '{:.' + str(n) + 'f}'
    print(string.format(pi))

# for running this script in command line
if __name__ == "__main__":
    import sys
    PI(int(sys.argv[1]))

