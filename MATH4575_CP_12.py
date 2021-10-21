# K = 133457799BBCDFF1
# x = 0123456789ABCDEF

K = [0, 0, 0, 1, 0, 0, 1, 1, 
      0, 0, 1, 1, 0, 1, 0, 0,
      0, 1, 0, 1, 0, 1, 1, 1,
      0, 1, 1, 1, 1, 0, 0, 1,
      1, 0, 0, 1, 1, 0, 1, 1,
      1, 0, 1, 1, 1, 1, 0, 0,
      1, 1, 0, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 0, 0, 0, 1]

x = [0, 0, 0, 0, 0, 0, 0, 1,
     0, 0, 1, 0, 0, 0, 1, 1,
     0, 1, 0, 0, 0, 1, 0, 1,
     0, 1, 1, 0, 0, 1, 1, 1,
     1, 0, 0, 0, 1, 0, 0, 1,
     1, 0, 1, 0, 1, 0, 1, 1,
     1, 1, 0, 0, 1, 1, 0, 1,
     1, 1, 1, 0, 1, 1, 1, 1]

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

C_ZERO = [1, 1, 1, 1, 0, 0, 0,
          0, 1, 1, 0, 0, 1, 1,
          0, 0, 1, 0, 1, 0, 1,
          0, 1, 0, 1, 1, 1, 1]

D_ZERO = [0, 1, 0, 1, 0, 1, 0,
          1, 0, 1, 1, 0, 0, 1,
          1, 0, 0, 1, 1, 1, 1,
          0, 0, 0, 1, 1, 1, 1]

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
  L0 = IPx[:31]
  R0 = IPx[32:]
  return (L0, R0)

# Returns a string that formats the input array into an n x m matrix
def formatMatrix(input, m):
  matrix = '['
  for i in range(len(input)):
    if i % m == 0 and i != 0:
      matrix += '\n '
    matrix += str(input[i])
  matrix += ']'
  return matrix

##### Answers #####

print('a. Key Schedule')
schedule = generateKeySchedule(K)
for i in range(len(schedule)):
      keyRound = ''.join([str(e) for e in schedule[i]])
      print(f'K{i + 1} = {keyRound}')

print('b. E(R0)')
(L0, R0) = getL0R0(x)
E_R0 = applyE(R0)
print(f'{formatMatrix(E_R0, 6)}')

print('c. L1')

print ('d. R1')