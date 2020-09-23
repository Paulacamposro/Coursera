def multiplica_matrizes(A, B):
    multiplica = []
    numA_lin = len(A)
    numA_col = len(A[0])
    numB_lin = len(B)
    numB_col = len(B[0])
    assert numA_col == numB_lin

    for i in range(numA_lin):
        multiplica.append([])
        for j in range(numB_col):
            multiplica[i].append(0)
            for k in range(numA_col):
                multiplica[i][j] += A[i][k] * B[k][j]
                
    return multiplica         

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    print(multiplica_matrizes(A, B))
