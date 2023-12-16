#Caesar's Cipher Encryption/Decryption App

def encode(message, shift):
    """Encode a message using Caesar's Cipher"""
    newMessage = ''
    for letter in message:
        position = alphabet.index(letter)
        newPosition = position + shift
        newLetter = alphabet[newPosition]
        newMessage += newLetter
    print(f"Message: {newMessage}")

def decode(message, shift):
    """Decode a message using Caesar's Cipher"""
    newMessage = ''
    for letter in message:
        position = alphabet.index(letter)
        newPosition = position + (-1 * shift)
        newLetter = alphabet[newPosition]
        newMessage += newLetter
    print(f"Message: {newMessage}")

#Intro
print('Welcome to the encoder.')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Inputs
choiceEnDe = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Encode/Decode message
if choiceEnDe == "encode":
    word = encode(message, shift)
else:
    word = decode(message, shift)

print(f'{word}')
