#Check the description to read the instructions for this task.
def tribonacci(signature, n):
    for i in range (n-3):
        signature.append(sum(signature[-3:]))
    return signature[:n]
