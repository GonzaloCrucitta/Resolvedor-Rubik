import time
import numpy as np
""" 
orientaciones esquinas:
0 => orientacion correcta
1 => girada en sentido horario
2 => girada en sentido antihorario

orientaciones aristas:
0 => orientacion correcta
1 => orientacion incorrecta
cubo = {
    esquinas_pos: [1,2,3,4,5,6,7,8],
    esquinas_ori: [0,0,0,0,0,0,0,0],
    aristas_pos: [1,2,3,4,5,6,7,8,9,10,11,12],
    aristas_ori: [0,0,0,0,0,0,0,0,0,0,0,0]
}
 """
""" 
def U(ep,eo,ap,ao):
    ep[], ep[], ep[], ep[] = ep[], ep[], ep[], ep[] 
    eo[], eo[], eo[], eo[] = eo[], eo[], eo[], eo[]

    ap[], ap[], ap[], ap[] = ap[], ap[], ap[], ap[]
    ao[], ao[], ao[], ao[] = ao[], ao[], ao[], ao[]
 """

def U(ep,eo,ap,ao):
    ep[2], ep[6], ep[7], ep[3] = ep[3], ep[2], ep[6], ep[7] 
    eo[2], eo[6], eo[7], eo[3] = eo[3], eo[2], eo[6], eo[7]

    ap[2], ap[5], ap[10], ap[6] = ap[6], ap[2], ap[5], ap[10]
    ao[2], ao[5], ao[10], ao[6] = ao[6], ao[2], ao[5], ao[10]

def Up(ep,eo,ap,ao):
    ep[2], ep[6], ep[7], ep[3] = ep[6], ep[7], ep[3], ep[2] 
    eo[2], eo[6], eo[7], eo[3] = eo[6], eo[7], eo[3], eo[2]

    ap[2], ap[5], ap[10], ap[6] = ap[5], ap[10], ap[6], ap[2]
    ao[2], ao[5], ao[10], ao[6] = ao[5], ao[10], ao[6], ao[2]

def U2(ep,eo,ap,ao):
    ep[2], ep[6], ep[7], ep[3] = ep[7], ep[3], ep[2], ep[6] 
    eo[2], eo[6], eo[7], eo[3] = eo[7], eo[3], eo[2], eo[6]

    ap[2], ap[5], ap[10], ap[6] = ap[10], ap[6], ap[2], ap[5]
    ao[2], ao[5], ao[10], ao[6] = ao[10], ao[6], ao[2], ao[5]


def D(ep,eo,ap,ao):
    ep[1], ep[5], ep[4], ep[0] = ep[5], ep[4], ep[0], ep[1] 
    eo[1], eo[5], eo[4], eo[0] = eo[5], eo[4], eo[0], eo[1]

    ap[0], ap[4], ap[8], ap[7] = ap[4], ap[8], ap[7], ap[0]
    ao[0], ao[4], ao[8], ao[7] = ao[4], ao[8], ao[7], ao[0]

def Dp(ep,eo,ap,ao):
    ep[1], ep[5], ep[4], ep[0] = ep[0], ep[1], ep[5], ep[4] 
    eo[1], eo[5], eo[4], eo[0] = eo[0], eo[1], eo[5], eo[4]

    ap[0], ap[4], ap[8], ap[7] = ap[7], ap[0], ap[4], ap[8]
    ao[0], ao[4], ao[8], ao[7] = ao[7], ao[0], ao[4], ao[8]

def D2(ep,eo,ap,ao):
    ep[1], ep[5], ep[4], ep[0] = ep[4], ep[0], ep[1], ep[5] 
    eo[1], eo[5], eo[4], eo[0] = eo[4], eo[0], eo[1], eo[5]

    ap[0], ap[4], ap[8], ap[7] = ap[8], ap[7], ap[0], ap[4]
    ao[0], ao[4], ao[8], ao[7] = ao[8], ao[7], ao[0], ao[4]

def prueba_tiempos():
    cubo = {
        "esquinas_pos": [1,2,3,4,5,6,7,8],
        "esquinas_ori": [0,0,0,0,0,0,0,0],
        "aristas_pos": [1,2,3,4,5,6,7,8,9,10,11,12],
        "aristas_ori": [0,0,0,0,0,0,0,0,0,0,0,0]
    }
    print("iniciando testeo con orientaciones...")
    inicio = time.time()
    for i in range (1000000):
        U(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"],cubo["aristas_ori"])
    fin = time.time()
    print("tiempo usando orientaciones: ",fin-inicio)
prueba_tiempos()



#0.1304 -> 0.2545 por tener orientaciones y un diseño distinto de cubo