#Check the description to read the instructions for this task.
def middle_permutation(string):
    new_string=[]
    string = [*string]
    string.sort()
    if len(string) % 2 == 0:
        new_string.append(string[(len(string)//2)-1])
        string.pop((len(string)//2)-1)
        string.reverse()
        for letter in string:
            new_string.append(letter)
    
    else:
        new_string.append(string[len(string)//2])
        string.pop(len(string)//2)
        new_string.append(string[(len(string)//2)-1])
        string.pop((len(string)//2)-1)
        string.reverse()
        for letter in string:
            new_string.append(letter)
    
    return "".join(new_string)

  
  
#As you might have noticed, you just can't calculate all the permutations because some tests that has like 13 letters. In that case you will have 6227020800 different permutations, which means that your script won't make it in time. Instead, I recognized the pattern of the middle element of all permutations (if they are sorted, which is the case). If the number of elements is even, the pattern is something like this:
#[n/2, followed by the rest of elements in reversed sort]. In case its odd: [n/2,(n/2)-1, followed by the rest of elements in reversed sort].
#Knowing that, I could write this script without having to calculate all the possible permutations.
