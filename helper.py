alpha = 'abcdefghijklmnopqrstuvwxyz'
def alphabet_position(letter):  
    
    for index, char in enumerate(alpha):
        if letter.lower() == char:
            return index

def rotate_character(char,rot):
    int_rot= int(rot)
    initial_pos= alphabet_position(char)
    new_pos= 0
    
    if not char.isalpha():
        return char
    if int_rot>26:
        int_rot = int_rot%26
        new_pos=initial_pos+int_rot
    if int_rot+initial_pos>25:
       
       new_pos= int_rot-(26-initial_pos)

    else:
        new_pos= initial_pos+int_rot
    
    for index, cha in enumerate(alpha):
        if index==new_pos:
            if char.isupper():
                return alpha[index].capitalize()
            else:
                return alpha[index]
