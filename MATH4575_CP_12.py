# K = 133457799BBCDFF1
# x = 0123456789ABCDEF

# K matrix
K = [0, 0, 0, 0, 0, 0, 1, 1, 
      0, 0, 1, 1, 0, 1, 0, 0,
      0, 1, 0, 1, 0, 1, 1, 1,
      0, 1, 1, 1, 1, 0, 0, 1,
      1, 0, 0, 1, 1, 0, 1, 1,
      1, 0, 1, 1, 1, 1, 0, 0,
      1, 1, 0, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 0, 0, 0, 1]

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
      output = input[times:len(input)]
      output.extend(input[0:times])
      return output

