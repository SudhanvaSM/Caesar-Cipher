def encode_or_decode (original_text, shift_amt, direction):         #funtion to encrypt or decrypt the message
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']        #list to check index of each element in the message

    if direction == 'decode':
        shift_amt *= -1        #multiplying by -1 so that the program decrypts by shifting the index backwards
    elif direction == 'encode':
        shift_amt *= 1
    else:
        print("Error")
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabets.index(letter) + shift_amt        #save the new element in message by adding the index of message with specified amount
        shifted_position %= len(alphabets)                            #to keep the loop in range of length of alphabets list
        cipher_text += alphabets[shifted_position]                    #append the new element into encrypted/decrypted string
    
    print(f"Here is the {direction}d result: {cipher_text}")

direction = input("Type 'encode' to encrypt or 'decode' to decrypt the message: ").lower()
text = input("Enter the message: ").lower()
shift = int(input("Enter the shift amount: "))

encode_or_decode (original_text = text, shift_amt= shift, direction = direction)


