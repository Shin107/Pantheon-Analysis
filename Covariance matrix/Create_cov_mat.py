import numpy as np
import pandas as pd

def replace_diagonal_blocks(small_matrix, large_matrix):
    n = int(large_matrix.shape[0]/3)
    for i in range(n):
        large_matrix[i*3:i*3+3, i*3:i*3+3] = small_matrix[i]
    return large_matrix

smallmat=np.array([[[str(k)+'_('+str(i)+','+str(j)+')' for i in range(3)] for j in range(3)]for k in ['x','y','z','a','b']])

testmat=np.zeros([15,15]).astype(str)
result = replace_diagonal_blocks(smallmat, testmat)
print(result)



result[3*3:3*3+3, 3*3:3*3+3] = np.ones([3,3])




PAN=pd.read_csv("Pantheon+SH0ES.csv",delimiter=' ')


s_x1_x0=PAN['COV_x1_x0']
s_c_x0=PAN['COV_c_x0']
s_x1_c=PAN['COV_x1_c']
x0=PAN['x0']

s_x1=np.array(PAN['x1ERR']**2)
s_c=np.array(PAN['cERR']**2)
s_mb=np.array(PAN['mBERR']**2)
s_x0=np.array(PAN['x0ERR'])

s_x1_mb=-2.5*(s_x1_x0)/(np.log(10)*x0)
s_c_mb=-2.5*(s_c_x0)/(np.log(10)*x0)
s_c_x0=PAN['COV_c_x0']
s_x1_c=PAN['COV_x1_c']
small_matrix=[]
for m in range(len(PAN)):
    #print(m)

    temp1=np.array([[0 for i in range(3)]for j in range(3)]).astype(float)
    temp1[0][1]=s_x1_mb[m]
    temp1[0,2]=s_c_mb[m]
    temp1[1,2]=s_x1_c[m]
    temp1[1,0]=temp1[0,1]
    temp1[2,0]=temp1[0,2]
    temp1[2,1]=temp1[1,2]
    temp1[1,1]=s_x1[m]
    temp1[2,2]=s_c[m]
    small_matrix.append(temp1)
small_matrix=np.array(small_matrix)

large_matrix=np.zeros([3*1701,3*1701])
result = replace_diagonal_blocks(small_matrix,large_matrix )


statsys=pd.read_csv("Pantheon+SH0ES_STAT+SYS.cov")
statsys1=np.array(statsys['1701'])
temp_2=np.reshape(statsys1,(1701,1701))
temp_2
temp3=np.zeros([3*1701,3*1701])
temp_ar=np.array([])
for i in range(1701):
    for j in range(1701):
        temp3[3*i,3*j]=temp_2[i,j]

stasys_final=temp3+result
#np.save('statsys_improved',statsys_final)
#s=np.load('statsys_improved.npy')


