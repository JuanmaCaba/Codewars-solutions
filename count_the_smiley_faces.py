#Check the description to read the instructions for this task.

def count_smileys(arr):
    valid_features = {"eyes":":;", "noses":"-~", "smiles":")D"}
    counter = 0
    if arr:
        for face in arr: 
            if len(face) == 2 and face[0] in valid_features["eyes"] and face[1] in valid_features["smiles"]:
                counter += 1

            if len(face) == 3 and face[0] in valid_features["eyes"] and face[1] in valid_features["noses"] and face[2] in valid_features["smiles"]:
                counter += 1
            
    return counter 
