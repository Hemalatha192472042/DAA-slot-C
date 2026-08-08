def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    P1 = strassen(add(A11, A22), add(B11, B22))
    P2 = strassen(add(A21, A22), B11)
    P3 = strassen(A11, sub(B12, B22))
    P4 = strassen(A22, sub(B21, B11))
    P5 = strassen(add(A11, A12), B22)
    P6 = strassen(sub(A21, A11), add(B11, B12))
    P7 = strassen(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(P1, P4), P5), P7)
    C12 = add(P3, P5)
    C21 = add(P2, P4)
    C22 = add(sub(add(P1, P3), P2), P6)

    new = []
    for i in range(mid):
        new.append(C11[i] + C12[i])
    for i in range(mid):
        new.append(C21[i] + C22[i])

    return new

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(strassen(A,B))
