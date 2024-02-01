encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

def decrypt_transposition(encrypted_text):
    
    char_list = list(encrypted_text)
   
    n = len(char_list)
    mid_point = n // 2
    
    
    start, end = 1, -2

    
    while start < mid_point:
        
        char_list[start], char_list[end] = char_list[end], char_list[start]
        start += 2
        end -= 2

    
    return ''.join(char_list)


with open('encrypted_message_two.txt', 'r') as file:
    encrypted_message = file.read().strip()


decrypted_message = decrypt_transposition(encrypted_message)
print(decrypted_message)
