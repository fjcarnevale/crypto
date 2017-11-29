
class Alphabet:
  
  def __init__(self, alphabet):
    self.alphabet = alphabet
    self.reverse_alphabet = {v: k for k, v in self.alphabet.iteritems()}

  def Encrypt(self, character):
    if character in self.alphabet:
      return self.alphabet[character]
    else:
      raise IndexError('Unknown character ' + character)

  def Decrypt(self, character):
    if character in reverse_alphabet:
      return reverse_alphabet[character]
    else:
      raise KeyError('Unknown character ' + character)

  @staticmethod
  def RotationAlphabet(n):
    return Alphabet({chr(i): chr(((i+1-96) % 26)+96) for i in range(97, 123)})
  
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







 
