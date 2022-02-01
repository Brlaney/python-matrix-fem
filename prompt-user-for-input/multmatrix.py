def multmatrix(a, b):
    # Returns the product of matrix a and matrix b.
    m1 = len(a)      # num of rows for matrix a (used as "m" in book)
    n1 = len(a[0])   # num of cols for matrix a
    m2 = len(b)      # num of rows for matrix b 
    n2 = len(b[0])   # num of cols for matrix b (used as "n" in book)
    newmatrix = []
    
    # Matrix mult only exists iff n1 equals m2
    if n1 == m2:
        for i in range(m1):
            row = []
            
            # For every column in b && for
            # every element in that column
            for j in range(n2):
                sum1 = 0
                for k in range(m2):
                    sum1 += a[i][k] * b[k][j]
                row.append(sum1)
            newmatrix.append(row)
        return newmatrix
    
    # If n1 != m2 then matrix mult is undefined
    else: 
        newmatrix = 'Does not exist'
    return newmatrix


# Test 1:
a1 = [[1, 2, -3, -1]]
b = [[4,-1], [-2,3], [6,-3], [1,0]]
print('\n' + 'Test 1 output: ')
print(multmatrix(a1, b)) 
# Expected output: [[-19, 14]]

# Test 2:
a2 = [[1, 2, -3]]
print('\n' + 'Test 2 output: ')
print(multmatrix(a2, b))
# Expected output: 'Does not exist.' since n1 != m2.
