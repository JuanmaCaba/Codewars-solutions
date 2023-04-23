#Check the description to read the instructions for this task.
def strip_comments(strng, markers):
    new_list = strng.splitlines()
    result_list = []
    if not markers:
        for line in new_list:
            result_list.append(line.rstrip())
    elif markers:        
        for line in new_list:
            markers_counter = 0
            for marker in markers:
                if marker not in line:
                    markers_counter += 1
                    if markers_counter == len(markers):
                        result_list.append(line.rstrip())            
            for index,letter in enumerate(line):
                if letter in markers:
                    result_list.append(line[:index].rstrip())
                    break
    return "\n".join(result_list)

