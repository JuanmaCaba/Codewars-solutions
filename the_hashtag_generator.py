#Check the description to read the instructions for this task.

def generate_hashtag(s):
    new_list = []
    for word in s.split(" "):
        new_list.append(word.title().strip())
    final_string = "".join(new_list)
    
    if len(final_string) >= 140 or s == "":
        return False
    elif final_string[0] == "#":
        return final_string
    else:
        return f"#{final_string}"
