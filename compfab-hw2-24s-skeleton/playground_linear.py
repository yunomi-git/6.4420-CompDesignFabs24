import numpy as np
dim = 3
dim2 = dim * dim

dFT_dF = np.zeros((dim2, dim2))
for i in range(dim):        # <--
    for j in range(dim):    # <--
        # In matrix block i,j, element j,i is 1
        # In the overall matrix, this is element i*dim + j, j*dim + i
        dFT_dF[i*dim + j, j*dim + i] = 1

print(dFT_dF)

D2 = np.zeros((dim2, dim2))
# The expression evaluates to Tr(dF/dF) * I, where Tr(dF/dF) = dim2
for i in range(dim):  # <--
    for j in range(dim):  # <--
        D2[i * dim + j, i*dim + j] = dim2
print(D2)