'''
    This program intends to find the RREF Form of any matrix that is given to it
    It does this through a (possibly) inefficient algorithm that I just came up with
    Good Luck, I did not bother writing comments.
    - DS, 07-06-23
'''
A = eval(input('Enter the matrix -> '))
m = []

for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] == 0:
            continue
        else:
            if A[i][j] != 1:
                sc = A[i][j]
                m.append('R'+str(i)+' -> '+'R'+str(i)+' / '+str(A[i][j]))
                for a in range(len(A[i])):
                    A[i][a] = A[i][a]/sc
                #print(m[-1])
                #print(A)
            break
    for x in range(len(A)):
        if x==i:
            continue
        else:
            piv = A[x][j]
            m.append('R'+str(x)+' -> '+'R'+str(x)+' - '+str(A[x][j])+' x R'+str(i))
            for y in range(len(A[x])):
                if A[x][y] == 0:
                    continue
                else:
                    A[x][y] = A[x][y] - piv*A[i][y]
            #print(m[-1])
            #print(A)


print('=============RESULTS=============')

print('The RREF Form -> ')
for i in A:
    print(i)
print('The Row Operations -> ')
for i in m:
    print(i)
