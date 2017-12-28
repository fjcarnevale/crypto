import utils

f = open('stage_2.txt', 'r')
ciphertext = f.read()
f.close()

#for i in range(25):
  # print utils.decipherRotation(ciphertext, i)

print utils.decipherRotation(ciphertext, 7)
