# Cryptosystem constants -----------------------------------------------------------------
# K = 133457799BBCDFF1
K = [0, 0, 0, 1, 0, 0, 1, 1, 
      0, 0, 1, 1, 0, 1, 0, 0,
      0, 1, 0, 1, 0, 1, 1, 1,
      0, 1, 1, 1, 1, 0, 0, 1,
      1, 0, 0, 1, 1, 0, 1, 1,
      1, 0, 1, 1, 1, 1, 0, 0,
      1, 1, 0, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 0, 0, 0, 1]

# x = 0123456789ABCDEF
X = [0, 0, 0, 0, 0, 0, 0, 1,
     0, 0, 1, 0, 0, 0, 1, 1,
     0, 1, 0, 0, 0, 1, 0, 1,
     0, 1, 1, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 1, 0, 0, 1,
     1, 0, 1, 0, 1, 0, 1, 1,
     1, 1, 0, 0, 1, 1, 0, 1,
     1, 1, 1, 0, 1, 1, 1, 1]

# DES-Cipher constants -------------------------------------------------------------------
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# S-box constants ------------------------------------------------------------------------
S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 1]]

S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [4, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 1]]
# ----------------------------------------------------------------------------------------

# Permutes the input based on the permutation described by 'indices'.
# e.g 
# - permute([10, 11, 12], [2, 3, 1]) => [11, 12, 10]
# - permute([10, 11, 12], [1, 1, 1, 2]) => [10, 10, 10, 11]
def permute(input, indices):
      output = []
      for i in indices:
            output.append(input[i - 1])
      return output

# Performs a left shift n times on the input.
# e.g
# - leftShift([1, 2, 3, 4, 5], 1) => [2, 3, 4, 5, 1]
# - leftShift([1, 2, 3, 4, 5], 7] => [3, 4, 5, 1, 2]
def leftShift(input, n):
      times = n % len(input)
      return input[times:len(input)] + input[0:times]

# Performs PC1 and returns C0 and D0.
# Takes an array of size 64 and returns a pair of arrays of size 28
def pc1(input):
      p1 = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36]

      p2 = [63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]
      return (permute(input, p1), permute(input, p2))

# Performs PC2 and a key round
# Takes two arrays of size 28 and returns an array of size 48
def pc2(input1, input2):
      p = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
      return permute(input1 + input2, p)

def v(input):
      if input in [1, 2, 9, 16]:
            return 1
      return 2

def generateKeySchedule(key):
      (C0, D0) = pc1(key)
      c = [C0]
      d = [D0]
      k = []
      for i in range(1, 17):
            ci = leftShift(c[i - 1], v(i))
            di = leftShift(d[i - 1], v(i))
            ki = pc2(ci, di)
            c.append(ci)
            d.append(ci)
            k.append(ki)
      return k

# Performs E: {0, 1}^32 -> {0, 1}^48
# Takes an array of size 32 and returns an array of size 48 that is permuted by E
def applyE(input):
  E = [32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1]
  return permute(input, E)

# Performs IP: {0, 1}^64 -> {0, 1}^64
# Takes an array of size 64 (x) and returns 2 arrays of size 32 (L0 and R0) that are permuted by IP
def getL0R0(input):
  IPx = permute(input, IP)
  L0 = IPx[:32]
  R0 = IPx[32:]
  return (L0, R0)

# Performs a round: f(A, J) = f(R^(i-1), K^i)
def round(A, J):
  XOR = xor(A, J)
  p = [16, 7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2, 8, 24, 14,
       32, 27, 3, 9,
       19, 13, 30, 6,
       22, 11, 4, 25]
  c = []
  for i in range(8):
    row = sbox(''.join(str(e) for e in XOR[i:i+5]), i)
    row_list = list([int(e) for e in row])
    for j in range(len(row_list)):
      c.append(row_list[j])
  return permute(c, p)

# Uses the s-box to return a new matrix
def sbox(s, n):
  sbox_n = {0: S1, 1: S2, 2: S3, 3: S4, 4: S5, 5: S6, 6: S7, 7: S8}
  row = int(s[0] + s[-1], 2)
  col = int(s[1:5], 2)
  box = sbox_n[n]
  return f'{box[row][col]:04b}'

# Returns a string that formats the input array into an n x m matrix
def formatMatrix(input, m):
  matrix = '['
  for i in range(len(input)):
    if i % m == 0 and i != 0:
      matrix += '\n '
    matrix += f'{str(input[i])} '
  end_index = len(matrix) - 1
  return matrix[:end_index] + ']'

# Takes two arrays of size 48 and returns an array of size 48 by XOR input1 with input2
def xor(input1, input2):
  xor = []
  for i in range(len(input1)):
    if input1[i] + input2[i] == 1:
      xor.append(1)
    else:
      xor.append(0)
  return xor

# R^i = L^(i-1) + f(R^(i-1), K^i)
def getR(L, R, K):
  f = round(R, K)
  return xor(L, f)

# Compute y: y = (IP^-1)(L^16, R^16), then convert to hex
# Returns a string representing the ciphertext
def y(L, R):
  # TODO: Implement
  return ''

# Encrypts the given plaintext using the given key with the DES-cipher
# Takes in two arrays representing the plaintext and key, and returns a string representing 
# the encrypted ciphertext
def descipherEncrypt(x, k):
  (L, R) = getL0R0(x)
  keySchedule = generateKeySchedule(k)
  # Perform each round until we get L^16 and R^16
  for i in range(16):
    prevL = L # L^(i-1)
    L = R # Update L to be R^(i-1)
    R = getR(prevL, R, keySchedule[i]) # Update R using L^(i-1), R^(i-1) and K^i
  ciphertext = y(L, R)
  return ciphertext

# Answer ---------------------------------------------------------------------------------
print(f'The ciphertext is y = {descipherEncrypt(X, K)}')
