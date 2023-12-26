from codes import codes

cipher_list = ["bee", "chai", "challah", "grapes", "horn", "scroll", "wine"]

#encryption function
def encrypt(code, message):

  cipher = codes[code]
  encrypted_message = ""
  
  for i in message:
    
    encrypted_message += cipher[i]

  return encrypted_message


#decryption function
def decrypt(code, message):

  decrypted_message = ""

  for i in message:

    decrypted_message += list(codes[code])[list(codes[code].values()).index(i)]

  return decrypted_message
  
  

#get user input for action and cipher
code = input("""Select a cipher:\n
  1: bee
  2: chai
  3: challah
  4: grapes
  5: horn
  6: scroll
  7: wine
  \n""")

print(f"\nCipher set to {cipher_list[int(code)-1]}\n")

action = input("Would you like to encrypt or decrypt? (e/d): ")

# perform encryption or decryption on given message
if (action == "e"):
  print("\nYou chose to encrypt.\n")
  message = input("Type message to encrypt:\n\n")
  message = message.lower()
  
  print(encrypt(code, message))

elif (action == "d"):
  print("\nYou chose to decrypt.\n")
  message = input("Type message to decrypt:\n\n")
  message = message.lower()

  print(decrypt(code, message))

else:
  print("Invalid option.")