def find_uniq(arr):
    temp_list = set(arr)
    for i in temp_list:
        if arr.count(i) == 1:
            return i
