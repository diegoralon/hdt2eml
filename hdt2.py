import numpy as np


# Problema 1 

m = np.array([[1,1,0,0,0,0,1],
[0,1,1,0,0,1,0], [0,0,1,1,0,0,0],
[0,0,0,1,1,0,1],[1,0,0,0,0,1,1],
[0,0,0,0,1,1,1],[1,1,1,0,0,0,1]])

m1 = np.array([[1,1,0,0,0,1,1],
[1,1,1,0,1,0,0], [0,1,1,1,1,0,0],
[0,0,1,1,0,0,1],[0,1,1,0,1,1,1],
[1,0,0,0,1,1,1],[1,0,0,1,1,1,1]
])

m2 = np.array([[1,1,0,0,0,0,0],
[1,1,0,0,0,0,0],[0,0,1,1,0,0,0],
[0,0,1,1,0,0,0],[0,0,0,0,1,1,1],[0,0,0,0,1,1,1],
[0,0,0,0,1,1,1]])

def reflexiva (m):
    if(np.diagonal(m).sum() == m.shape[0]):
        print('Es Reflexiva')
    else: 
        print('No es Reflexiva')

reflexiva(m)  
reflexiva(m1)  
reflexiva(m2)     

def simetrica (m): 
    if ((m == np.transpose(m)).all()):
        print('Es Simetrica')
    else:
        print('No es Simetrica')

simetrica(m)
simetrica(m1)
simetrica(m2)


    


# Problema 2

A = np.arange(5,9).reshape(2,2)


B = np.arange(-7,-1).reshape(2,3)


C = np.arange(4,14,3).reshape(2,2)

D = np.eye(2)

E = np.zeros(6).reshape(2,3)

# Parte de arriba

arriba = np.hstack([A,D,E])
abajo = np.hstack([D,C,B])

F = np.vstack([arriba,abajo])
print(F)

# Problema 3 

# A favor de las manijas del reloj

p1 = np.arange(0,24).reshape(4,6)
p2 = np.array([1,2,3])
print(p1)

def rota90 (m): 
    x = np.transpose(m)
    print('Rota 90 grados \n', np.flip(x,0))

def rota180 (m): 
    x = np.flip(m)
    print('Rota 180 grados \n', x)

def rota270 (m): 
    x = np.flip(m,0)
    print('Rota 270 grados \n', np.transpose(x))

rota90(p1)
rota180(p1)
rota270(p1)

def rota90_otrolado (m): 
    x = np.transpose(m)
    print('Rota 90 grados \n', np.flip(x,1))

def rota180_otrolado (m): 
    x = np.flip(m)
    print('Rota 180 grados alrevez \n', x)

def rota270_otrolado (m):
    x = np.transpose(m)
    print('Rota 270 grados alrevez \n', np.flip(x,0))

rota90_otrolado(p1)
rota180_otrolado(p1)
rota270_otrolado(p1)

# Problema 4

coeficientes = np.array([[2,0,0,1,0,0,0,0],
[1,0,0,1,0,0,0,0],[-1,0,0,2,0,0,0,0],
[0,2,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],
[0,-1,0,0,2,0,0,0],[0,0,2,0,0,1,0,0],
[0,0,1,0,0,1,0,0],[0,0,-1,0,0,2,0,0],
[0,0,0,0,0,0,1,2],[0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,2,-1]])

iguales = np.array([[4],[3],[3],[3],[2],[1],[6],[4],[2]
,[-3],[-1],[4]])


inversa = np.linalg.pinv(coeficientes)

resultados = np.matmul(inversa,iguales)
print('Solución Matriz \n', resultados)






