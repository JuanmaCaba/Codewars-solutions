#Check the description to read the instructions for this task.

def order(sentence):
    if sentence:
        new_list = []
        index = 1
        while len(new_list) != len(sentence.split(" ")):
            for word in sentence.split(" "):
                for letter in word:
                    if letter == str(index):
                        new_list.append(word)
                        index+=1
                        
        return " ".join(new_list)
    else:
        return ""
