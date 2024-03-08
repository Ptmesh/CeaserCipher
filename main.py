alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from logo import logo

print(logo)
shouldContinue =  True

while shouldContinue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt \n")
    text = input("Type your message \n").lower()
    shiftNum = int(input("Enter the shift number \n"))


    def ceaser(text ,shift , direction):
        cipherText = ""
        for letter in text:
            position = alphabet.index(letter)
        if direction == "encode":
                for letter in text:
                    position = alphabet.index(letter)
                    newPosition = position + shift
                    newLetter = alphabet[newPosition]
                    cipherText += newLetter
                print(f"The encoded string is {cipherText}\n")
        elif direction == "decode":
                for letter in text:
                    position = alphabet.index(letter)
                    oldPosition = position - shift
                    oldLetter = alphabet[oldPosition]
                    cipherText += oldLetter
                print(f"The decoded string is {cipherText}\n")


    ceaser(text , shiftNum , direction)
    result = input("Do you want to continue Y or N \n").lower()
    if result == "N":
        shouldContinue = False
        print("GoodBye!!")
