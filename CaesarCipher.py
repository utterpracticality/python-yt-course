print("Welcome to the Caesar Cipher Encoder/Decoder!\n")

# Get input text (message that will be encrypted)
input_message = input("Enter message to be modified: ")

# Get the shift value
shift_value = int(input("Enter shift value (integer; Enter negative shift value to decrypt.): "))

# Define alphabet as a string
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Convert input text to cipher text
result = []

for char in input_message:
    if char.isalpha():
        is_upper = char.isupper()
        char = char.lower()
        index = alphabet.index(char)
        shifted_index = (index + shift_value) % 26
        shifted_char = alphabet[shifted_index]
        if is_upper:
            shifted_char = shifted_char.upper()
        result.append(shifted_char)
    else:
        result.append(char)

output_message = "".join(result)

# Print the cipher
print(f"Original message: {input_message}")
print(f"Modified message: {output_message}")