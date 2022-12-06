from cryptography.fernet import Fernet

def caesarEncrypt(text, numOfShifts):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + numOfShifts-65) % 26 + 65)
      else:
         result += chr((ord(char) + numOfShifts-97) % 26 + 97)
    return result

def caesarDecrypt(text, numOfShifts):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) - numOfShifts-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) - numOfShifts-97) % 26 + 97)
    return result



text = input("\nEnter the text: ")
encryptionAlgo = input("Enter encryption algorithm [caesar, fernet] : ")

if encryptionAlgo == 'fernet':
   key = Fernet.generate_key()
   f = Fernet(key)
   token = f.encrypt(text.encode())

   print(f"\n--->Fernet cipher text: {token.decode()}")

   text = f.decrypt(token)
   print(f"--->Plain text: {text.decode()}")

elif encryptionAlgo == 'caesar':
   numOfShifts = int(input("\nEnter the number shifts: "))
   print(f"\n--->Shift pattern : {numOfShifts}")

   encryptedText = caesarEncrypt(text, numOfShifts)
   print(f"--->Caesar cipher text: {encryptedText}")

   decryptedText = caesarDecrypt(encryptedText, numOfShifts)
   print(f"--->Plain text: {decryptedText}")


