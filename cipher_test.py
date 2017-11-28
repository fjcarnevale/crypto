from cipher import Cipher

c = Cipher()
#c.setCiphertext('the quick brown fox jumps over the lazy dog')

#c.frequencyAnalysis()

c.plaintext = 'aabbcc'
c.cipher_alphabet = 'cab'

m = c.encipher()

print m

print c.decipher(m)
