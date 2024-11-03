import random
import time

def merge(left: list, right: list):
    result = []
    while left != [] and right != []:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left + right
    return result

def merge_sort(arr):
    l = len(arr)
    if l == 1:
        return arr
    
    left = merge_sort(arr[:l//2])
    right = merge_sort(arr[l//2:])

    # print("left:", left)
    # print("right:", right)

    result = merge(left, right)
    # print("sorted:", result, "\n")

    return result


def main():
    array = [int(i) for i in input().split()]
    # array = [random.randrange(0,1000000) for _ in range(300000)]
    
    # print(array)
    result = merge_sort(array)
    print(' '.join(str(num) for num in result))


if __name__ == "__main__":
    # begin = time.time()
    main()
    # end = time.time()
    # print(f"Execution time: {end - begin: .3f}")