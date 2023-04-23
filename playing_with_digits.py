#CHeck the description to see the task given.
def dig_pow(n, p):
    new_list = [int(num)**(p+i) for i, num in enumerate(str(n))]
    final_num = sum(new_list)
    if final_num % n == 0:
        return final_num / n
    else: 
        return -1
