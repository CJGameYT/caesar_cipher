secret_message = "Somewhere over the rainbow 123"
number = 1

def caesar_cipher(text: str, shift: int):
    result = "" 
    
    for char in text:
        if char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            result += char 

    return result

def caesar_decipher(secret_message: str, shift: int):
    result = ""
    
    for char in secret_message:
        if char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) - shift - 48) % 10 + 48)
        else:
            result += char 

    return result

secret_message = caesar_cipher(secret_message, number)

print(caesar_cipher(secret_message, number))
print(caesar_decipher(secret_message, number))