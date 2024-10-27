def encode_or_decode (original_text, shift_amt, direction):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if direction == 'decode':
        shift_amt *= -1
    elif direction == 'encode':
        shift_amt *= 1
    else:
        print("Error")
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabets.index(letter) + shift_amt
        shifted_position %= len(alphabets)
        cipher_text += alphabets[shifted_position]
    
    print(f"Here is the {direction}d result: {cipher_text}")

direction = input("Type 'encode' to encrypt or 'decode' to decrypt the message: ").lower()
text = input("Enter the message: ").lower()
shift = int(input("Enter the shift amount: "))

encode_or_decode (original_text = text, shift_amt= shift, direction = direction)


