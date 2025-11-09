#Giros basicos del cubo, en sentido horario


# [1,2,3,4,5,6,7,8, 1,2,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10,11,12] cubo
# [0,1,2,3,4,5,6,7, 8,9,10,11,12,13,14,15,16,17,18,19] pos en array

def U(cubo):
    # [1,2, 3,4, 5,6, 7,8,  1,2, 3,4, 5, 6,7, 8,9,10, 11, 12] -> 
    # [1,2, 4,8, 5,6, 3,7,  1,2, 7,4, 5, 3,11, 8,9,10, 6, 12]

    #rotar esquinas
    cubo[2], cubo[6], cubo[7], cubo[3] = cubo[3], cubo[2], cubo[6], cubo[7]

    #rotar aristas
    cubo[10], cubo[13], cubo[18], cubo[14] = cubo[14], cubo[10], cubo[13], cubo[18]

    return cubo

def R(cubo):
    #rotar esquinas
    cubo[3], cubo[7], cubo[4], cubo[0] = cubo[0], cubo[3], cubo[7], cubo[4]

    #rotar aristas
    cubo[4], cubo[7], cubo[12], cubo[8] = cubo[8], cubo[4], cubo[7], cubo[12]
""" 
def L(cubo):
    cubo[], cubo[], cubo[], cubo[] = cubo[], cubo[], cubo[], cubo[]
    cubo[], cubo[], cubo[], cubo[] = cubo[], cubo[], cubo[], cubo[]
def F(cubo):
def D(cubo):
def B(cubo):

#Giros 'prima', en sentido antihorario
def Up(cubo):
def Rp(cubo):
def Lp(cubo):
def Fp(cubo):
def Dp(cubo):
def Bp(cubo):

#Giros dobles, de 180 grados
def UU(cubo):
def RR(cubo):
def LL(cubo):
def FF(cubo):
def DD(cubo):
def BB(cubo): 
"""