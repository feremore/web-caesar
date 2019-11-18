from helper import alphabet_position, rotate_character

def encrypt(text,rot):
    encrypted = ''
    for char in text:
        encrypted+= rotate_character(char,rot)
    return encrypted
        
def main():
    user_input= input('Type a message:\n')
    rotate_input= input("Rotate by:\n")
    print(encrypt(user_input,int(rotate_input)))

if __name__=="__main__":
    main()