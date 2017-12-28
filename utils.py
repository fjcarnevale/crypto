cipherbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plainbet  = 'abcdefghijklmnopqrstuvwxyz'

def frequencyAnalysis(ciphertext, isFile = False):
  if isFile:
    f = open(ciphertext, 'r')
    ciphertext = f.read()
    f.close()

  frequency_map = {}
  letter_count = 0
  for letter in [letter for letter in ciphertext if letter in cipherbet]:
    letter_count += 1
    if letter not in frequency_map:
      frequency_map[letter] = 1
    else:
      frequency_map[letter] += 1

  letters = frequency_map.keys()
  letters.sort()

  for letter in letters:
    print (
      letter
      + ': ' 
      + str(frequency_map[letter])
      + '  '
      + str(frequency_map[letter] * 100.0 / letter_count))


def decipher(ciphertext, key, isFile = False):
  if isFile:
    f = open(ciphertext, 'r')
    ciphertext = f.read()
    f.close()

  return ''.join([key[letter] if letter in key else letter for letter in ciphertext])


def decipherRotation(ciphertext, rotation):
  plaintext = ''
  for letter in ciphertext.lower():
    if letter in plainbet:
      rotated = ord(letter) - rotation
      if rotated < 97:
        rotated += 26
      plaintext += chr(rotated)
    else:
      plaintext += letter
  return plaintext


def remainingCipherbet(key):
  return [letter for letter in cipherbet if letter not in key]

def remainingPlainbet(key):
  return [letter for letter in plainbet if letter not in key.values()]
