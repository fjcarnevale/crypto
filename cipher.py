

class Cipher:

  def __init__(self):
    self.plaintext = ''
    self.ciphertext = ''
    self.cipher_alphabet = ''

  def frequencyAnalysis(self):
    frequency_map = {}
    for letter in self.ciphertext:
      if letter not in frequency_map:
        frequency_map[letter] = 1
      else:
        frequency_map[letter] += 1

    letters = frequency_map.keys()
    letters.sort()

    for letter in letters:
      print letter + ': ' + str(frequency_map[letter])

  def setCiphertext(self, ciphertext):
    self.ciphertext = ciphertext.upper()

  def encipher(self):
    message = [self.cipher_alphabet[ord(letter) - 97] for letter in self.plaintext]
    return ''.join(message).upper() 

  def decipher(self, ciphertext):
    message = [chr(self.cipher_alphabet.index(letter) + 97) for letter in ciphertext.lower()]
    return ''.join(message)







 
