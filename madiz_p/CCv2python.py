from PIL import Image, ImageEnhance
import numpy as np
import time

#import numpy as np

def Mean(mass, ddof = 0):
    '''
    Returns mean value of massive of values
    '''
    return sum(mass) / (len(mass) - ddof)


def Cov_matrix(mass_points):
    '''
    Counts covariant matrix of massive of 2D vectors (dots)
    '''

    # Count mean values

    M_0 = Mean([point[0] for point in mass_points])
    M_1 = Mean([point[1] for point in mass_points])
#    print(M_0, M_1)


    # Count covariations
    cov_00 = Mean([(point[0] - M_0)**2 for point in mass_points], ddof = 1)
    cov_11 = Mean([(point[1] - M_1)**2 for point in mass_points], ddof = 1)

    cov_01 = Mean([(point[0] - M_0)*(point[1] - M_1) for point in mass_points], ddof = 1)


    return [[cov_00, cov_01], [cov_01, cov_11]]


def EigenValues(matrix):
    '''
    Evaluates eigenvalues of 2D matrix
    '''

    D_sqrt = ((matrix[0][0]-matrix[1][1])**2 + 4*matrix[0][1]*matrix[1][0])**0.5
    lamb_1 = (matrix[0][0] + matrix[1][1] + D_sqrt) / 2
    lamb_2 = (matrix[0][0] + matrix[1][1] - D_sqrt) / 2


    return [lamb_1, lamb_2]


'''
def EigenVectors(matrix, v_lamb):

    Evaluates eigenvectors, using eigenvalues and 2D matrix
    
    if matrix[0][1] != 0:
        k_1 = (v_lamb[0] - matrix[0][0]) / matrix[0][1]
        k_2 = (v_lamb[1] - matrix[0][0]) / matrix[0][1]
    else:
        k_1 = (v_lamb[0] - matrix[0][0]) * 1e10
        k_2 = (v_lamb[1] - matrix[0][0]) * 1e10

    vec_1 = [1 / (k_12 + 1)0.5, k_1 / (k_12 + 1)0.5]
    vec_2 = [1 / (k_22 + 1)0.5, k_2 / (k_22 + 1)0.5]


    return [vec_1, vec_2]
'''


def PCA_analyse(mass_points):
    '''
    Summarise all process of PCA and returns ratio of eiginvalues
    ratio ~ 0 --> points form a LINE
    ratio ~ 0.3 - 0.5 --> points form a SPOT
    '''

    cov_matrix = Cov_matrix(mass_points)
    v_lamb = EigenValues(cov_matrix)


    return min(v_lamb) / max(v_lamb)

def N_S(i,j):
    all_brights1[i][j]=0
    
    if all_brights1[i+1][j] == 1:
        all_brights1[i+1][j]=0
        N.append((i+1,j))

    if all_brights1[i+1][j] == 2:
        all_brights1[i+1][j]=0
        S.append((i+1,j))
        
    if all_brights1[i+1][j+1] == 1:
        all_brights1[i+1][j+1]=0
        N.append((i+1,j+1))

    if all_brights1[i+1][j+1] == 2:
        all_brights1[i+1][j+1]=0
        S.append((i+1,j+1))
        
    if all_brights1[i+1][j-1] == 1:
        all_brights1[i+1][j-1]=0
        N.append((i+1,j-1))
    
    if all_brights1[i+1][j-1] == 2:
        all_brights1[i+1][j-1]=0
        S.append((i+1,j-1))
        
    if all_brights1[i][j+1] == 1:
        all_brights1[i][j+1]=0
        N.append((i,j+1))
    
    if all_brights1[i][j+1] == 2:
        all_brights1[i][j+1]=0
        S.append((i,j+1))
            
    if all_brights1[i][j-1] == 1:
        all_brights1[i][j-1]=0
        N.append((i,j-1))
        
    if all_brights1[i][j-1] == 2:
        all_brights1[i][j-1]=0
        S.append((i,j-1))
         
    if all_brights1[i-1][j+1] == 1:
        all_brights1[i-1][j+1]=0
        N.append((i-1,j+1))
        
    if all_brights1[i-1][j+1] == 2:
        all_brights1[i-1][j+1]=0
        S.append((i-1,j+1))
         
    if all_brights1[i-1][j] == 1:
        all_brights1[i-1][j]=0
        N.append((i-1,j))
        
    if all_brights1[i-1][j] == 2:
        all_brights1[i-1][j]=0
        S.append((i-1,j))
        
    if all_brights1[i-1][j-1] == 1:
        all_brights1[i-1][j-1]=0
        N.append((i-1,j-1))
        
    if all_brights1[i-1][j-1] == 2:
        all_brights1[i-1][j-1]=0
        S.append((i-1,j-1))
        
const1 = 117
const2 = 20
img = Image.open("test3.png").convert("L")
all_brights = np.asarray(img, dtype='uint8')
const_br1 = np.sum(all_brights ) / (img.size[0] * img.size[1]) + const1
const_br2 = np.sum(all_brights ) / (img.size[0] * img.size[1]) + const2

all_brights1 = all_brights.copy() # В all_brights1 будут 0, 1, 2

all_brights1[all_brights<const_br2] = 0
all_brights1[all_brights>const_br1] = 1 
all_brights1[(all_brights<const_br1) & (all_brights>const_br2)] = 2
all_C = []
N=[]
S=[]
while 1 in all_brights1:
    C = []
    i=np.where(all_brights1 == 1)[0][0]
    j=np.where(all_brights1[i] == 1)[0][0]
    print(i,j)
    C.append((i,j))
    N_S(i,j)
    while len(N)+len(S)>0:
        while len(N)==0:
            if len(S)>0:
                N_S(S[0][0],S[0][1])
                del S[0]
            if len(S)==0:
                break
        if len(N)==0:
            break
        C.append(N[0])
        N_S(N[0][0],N[0][1])
        del N[0]
    if len(C)>=3:
        if PCA_analyse(C)>0.3:
            all_C.append("particle")
        else:
            all_C.append("treck")
    else:
        all_C.append("particle")
print(f"количество треков:{all_C.count('treck')}")
print(f"количество частиц:{all_C.count('particle')}")
        
        
        
            
