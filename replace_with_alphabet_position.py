#Check the description to read the instructions for this task.
def alphabet_position(text):
    dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_string = []
    for i in text.lower():
        try:
            new_string.append(str(dictionary.index(i) + 1))
            new_string.append(" ")
        except ValueError:
            pass
    return "".join(new_string[:-1])
