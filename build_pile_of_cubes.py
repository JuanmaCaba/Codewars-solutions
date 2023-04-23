#Check the description to read the instructions for this task.
def find_nb(m):
    acumulated_mass = 0
    increment = 1
    while acumulated_mass < m:
        acumulated_mass += increment**3
        if acumulated_mass == m :
            return increment 
        increment +=1 
    return -1
