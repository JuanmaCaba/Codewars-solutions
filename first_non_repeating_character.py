#Check the description to read the instructions for this task.
def first_non_repeating_letter(string):
    new_string = string.lower()
    for index,letter in enumerate(new_string):
        if new_string.count(letter) == 1:
            return string[index]
    return ""
