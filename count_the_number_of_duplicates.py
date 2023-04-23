#Check the description to read the instructions for this task.
def duplicate_count(text):
    counter = 0
    repeated = []
    for letter in text.lower():
        if text.lower().count(letter) > 1 and letter not in repeated:
            counter += 1
            repeated.append(letter)
    return counter
