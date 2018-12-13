"""
Thought on the question:
Difficulty: Easy.
"""
import sys

def main():
    n,k = sys.stdin.readline().split()
    arr = sys.stdin.readline().split()
    result = []
    i = 0
    while True:
        if i >= len(arr):
            break
        if arr[i] == "undo":
            result = result[:-int(arr[i+1])]
            i = i + 2
            continue
        result.append(int(arr[i]))
        i += 1
    total = sum(result)
    outcome  = total % int(n)
    print(outcome)
if __name__ == "__main__":
    main()