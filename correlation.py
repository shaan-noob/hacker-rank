import math

def P(A, B):
    n = float(len(A))
    muA = sum(A) / n
    muB = sum(B) / n
    diffA = map(lambda x: x - muA, A)
    diffB = map(lambda x: x - muB, B)
    stdA = math.sqrt((1 / (n - 1)) * sum([d * d for d in diffA]))
    stdB = math.sqrt((1 / (n - 1)) * sum([d * d for d in diffB]))
    return (sum([A[i] * B[i] for i in range(int(n))]) - n * muA * muB) / ((n - 1) * stdA * stdB)

A = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
B = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
print('%.3f' % (P(A, B)))