alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode(message_to_encode):
    for letter in range(len(message_to_encode)):
        for j in range(len(alphabet)):
            if message_to_encode[letter] == alphabet[j]:
                message_to_encode[letter] = alphabet[(j + shift) % 26]
                break
    return message_to_encode


def decode(message_to_decode):
    for letter in range(len(message_to_decode)):
        for j in range(len(alphabet)):
            if message_to_decode[letter] == alphabet[j]:
                message_to_decode[letter] = alphabet[(j - shift) % 26]
                break
    return message_to_decode


answer = True
while answer:
    command = input("Type 'encode' or 'decode' message: \n").lower()
    if command == 'encode':
        str_to_encode = input("Type your message: \n")
        shift = int(input("Please type a shift: \n"))
        characters_to_encode = list(str_to_encode)
        encoded_message = encode(characters_to_encode)
        print("Encoded message: ", end="")
        for char in encoded_message:
            print(char, end="")

    elif command == 'decode':
        str_to_decode = input("Type your message to decode: \n").lower()
        shift = int(input("Please type a shift: \n"))
        characters_to_decode = list(str_to_decode)
        decoded_message = decode(characters_to_decode)
        print("Decoded message: ", end="")
        for char in decoded_message:
            print(char, end="")

    print()
    chose = input("Type 'yes' if you want to continue. And 'no' if you want to exit'\n")
    if chose == 'yes':
        answer = True
    if chose == 'no':
        print("Goodbye!")
        answer = False