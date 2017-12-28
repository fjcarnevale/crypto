import utils

utils.frequencyAnalysis('stage_1.txt', True)

key = {
  'X': 'e',
  'M': 'a',
  'J': 't',
  'P': 'h',
  'T': 'n',
  'N': 'd',
  'B': 'i',
  'R': 's', #??
  'H': 'k',
  'W': 'g',
  'C': 'o',
  'I': 'f',
  'Y': 'w',
  'L': 'm',
  'D': 'v',
  'V': 'r',
  'G': 'l',
  'U': 'u',
  'A': 'c',
  'Q': 'p',
  'F': 'b',
  'E': 'y',
  'S': 'j',
  'O': 'z',
  'K': 'q',
  'Z', 'x'
}

print utils.decipher('stage_1.txt', key, True)
print utils.remainingCipherbet(key)
print utils.remainingPlainbet(key)
