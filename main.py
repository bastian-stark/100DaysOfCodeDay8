def encode(message, shift):
    newMessage = ''
    for letter in message:
        position = alphabet.index(letter)
        newPosition = position + shift
        newLetter = alphabet[newPosition]
        newMessage += newLetter
    print(f"Message: {newMessage}")

def decode(message, shift):
    newMessage = ''
    for letter in message:
        position = alphabet.index(letter)
        newPosition = position + (-1 * shift)
        newLetter = alphabet[newPosition]
        newMessage += newLetter
    print(f"Message: {newMessage}")

print('Welcome to the encoder.')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

choiceEnDe = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if choiceEnDe == "encode":
    word = encode(message, shift)
else:
    word = decode(message, shift)

print(f'{word}')