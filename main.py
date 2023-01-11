def find_uniq(arr):
    find_dublicates(arr)
    
    return n   # n: unique number in the array


def find_dublicates(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i


