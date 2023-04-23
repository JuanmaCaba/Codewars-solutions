#Check the description to read the instructions for this task.
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        
   #Encode function 
    def encode(self, text):
        encripted_string = []
        for i, letter in enumerate(text):
            if letter in self.alphabet:
                abc_text_index = self.alphabet.index(letter)
                try:
                    abc_key_index = self.alphabet.index(self.key[i])
                except IndexError:
                    new_index = (i % len(self.key))
                    abc_key_index = self.alphabet.index(self.key[new_index])
    
                if (abc_text_index + abc_key_index) > (len(self.alphabet)-1):
                    encripted_string.append(self.alphabet[(abc_text_index + abc_key_index) - len(self.alphabet)])
                else:
                    encripted_string.append(self.alphabet[abc_text_index + abc_key_index])
            else:
                encripted_string.append(letter)
            
        return "".join(encripted_string)
                  
    #Decode function    
    def decode(self, text):
        decripted_string = []
        for i, letter in enumerate(text):
            if letter in self.alphabet:
                abc_text_index = self.alphabet.index(letter)
                try:
                    abc_key_index = self.alphabet.index(self.key[i])
                except IndexError:
                    new_index = (i % len(self.key)) 
                    abc_key_index = self.alphabet.index(self.key[new_index])
                         
                if (abc_text_index - abc_key_index) < 0:
                    decripted_string.append(self.alphabet[(abc_text_index - abc_key_index) + len(self.alphabet)])
                else:
                    decripted_string.append(self.alphabet[abc_text_index - abc_key_index])
            else:
                decripted_string.append(letter)
        return "".join(decripted_string)
