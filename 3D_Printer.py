import sys
import math
def main():
    a = int(sys.stdin.readline())
    n = math.ceil(math.log(a,2)) + 1
    print(n)

if __name__ == "__main__":
    main()