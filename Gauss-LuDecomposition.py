#Naseem Ali
def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""
    # Converts N into a list of tuples of columns
    tuple_N = zip(*N)
    # Nested list comprehension to calculate matrix multiplication
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def pivot_matrix(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)
    # Create an identity matrix, with floating point values
    id_matrix = [[float(i ==j) for i in xrange(m)] for j in xrange(m)]
    # Rearrange the identity matrix such that the largest element of
    # each column of M is placed on the diagonal of of M
    for j in xrange(m):
        row = max(xrange(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            # Swap the rows
            id_matrix[j], id_matrix[row] = id_matrix[row], id_matrix[j]

    return id_matrix

def lu_decomposition(arr):
    """Performs an LU Decomposition of A, The function returns P, L and U."""
    n = len(arr)
    # Create zero matrices for L and U
    L = [[0.0] * n for i in xrange(n)]
    U = [[0.0] * n for i in xrange(n)]
    # Create the pivot matrix P and the multipled matrix PA
    P = pivot_matrix(arr)
    PA = mult_matrix(P, arr)
    # Perform the LU Decomposition
    for j in xrange(n):
        # All diagonal entries of L are set to unity
        L[j][j] = 1.0

        for i in xrange(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in xrange(i))
            U[i][j] = PA[i][j] - s1

        for i in xrange(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in xrange(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]

    return (P, L, U)


def gauss(arr):
    m = len(arr)
    assert all([len(row) == m + 1 for row in arr[1:]]), "Matrix rows have non-uniform length must be 3!"
    n = m + 1
    
    for k in range(m):
        pivots = [abs(arr[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k
        
        # Check for singular matrix
        assert arr[i_max][k] != 0, "Matrix is unique!"
        
        # Swap rows
        arr[k], arr[i_max] = arr[i_max], arr[k]

        
        for i in range(k + 1, m):
            f = arr[i][k] / arr[k][k]
            for j in range(k + 1, n):
                arr[i][j] -= arr[k][j] * f

            # Fill lower triangular matrix with zeros:
            arr[i][k] = 0
    # Solve equation Ax=b for an upper triangular matrix A
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, arr[i][m] / arr[i][i])
        for k in range(i - 1, -1, -1):
            arr[k][m] -= arr[k][i] * x[0]
    return x

def isDm(arr,n):
    """Checking the len of arr, return true if less then 3, otherwise false"""
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            count = count + abs(arr[i][j])
        count = count - abs(arr[i][i])
        if (abs(arr[i][i]) < count):
            return False
    return True
    
if __name__ == "__main__":
    arr = [[10, 8, 1, -7], [4, 10, -5, 2], [5, 1, 10, 1.5]]
    arrSize = 3
    if(isDm(arr,arrSize)):
        print('Array size is lower than 4!')
        y = gauss(arr)
        print("X:")
        print(y)
    else:
        print('Array size is equal/bigger than 4!')
        P, L, U = lu_decomposition(arr)
        print("L:")
        print(L)
        print("U:")
        print(U)

