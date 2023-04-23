#Check the description to read the instructions for this task.

def find_even_index(arr):
    for index, x in enumerate(arr):
        lsum = sum(arr[0:index])
        rsum = sum(arr[index+1:])
        if lsum == rsum:
            return index
    return -1
