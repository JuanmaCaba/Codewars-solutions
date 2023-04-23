#Check the description to read the instructions for this task.

def move_zeros(lst):
    ceros = 0
    new_list = []
    for i in lst:
        if i != 0:
            new_list.append(i)
        else:
            ceros+=1
    for i in range(ceros):
        new_list.append(0)
    
    return new_list
