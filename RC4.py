import numpy as np


Plaintext = np.array([1, 3, 1, 2])
Ciphertext = np.array([0, 0, 0, 0])
Key = np.array([2, 6, 1, 5])
StateVector = np.array([0, 1, 2, 3, 4, 5, 6, 7])
KeyStream = np.array([2, 6, 1, 5, 2, 6, 1, 5])

print("The given plain text is : ")
print(Plaintext)
print("The given key is :")
print(Key)

j = 0
for i in range(8):
    j = (j + StateVector[i] + KeyStream[i]) % 8
    StateVector[i], StateVector[j] = StateVector[j], StateVector[i]

print("The state vector afer KSA phase is:")
print(StateVector)

i = j = 0
for k in range (4):
    i = (i + 1) % 8
    j = (j + StateVector[i]) % 8
    StateVector[i], StateVector[j] = StateVector[j], StateVector[i]
    Ciphertext[k] = ord(chr(Plaintext[k]))^(StateVector[(StateVector[i] + StateVector[j]) % 8])

print("The cipher text generated after PRGA phase is: ")
print(Ciphertext)

