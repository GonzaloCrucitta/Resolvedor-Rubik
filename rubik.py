import girosv2

cubo = {
        "esquinas_pos": [0,1,2,3,4,5,6,7],
        "esquinas_ori": [0,0,0,0,0,0,0,0],
        "aristas_pos": [0,1,2,3,4,5,6,7,8,9,10,11],
        "aristas_ori": [0,0,0,0,0,0,0,0,0,0,0,0]
    }

nodo ={
    "ultimo_giro", #U,R,2L,Fp, ...
    "cubo",
    "nodos_Sig"  #[]
}


def print_cube(cubo, giro):
    print("=== ",giro," ===")
    print("Esquinas:")
    for i, (p, o) in enumerate(zip(cubo["esquinas_pos"],cubo["esquinas_ori"])):
        print(f"  {i}: pos={p}, ori={o}")
    """ print("\nAristas:")
    for i, (p, o) in enumerate(zip(cubo["aristas_pos"], cubo["aristas_ori"])):
        print(f"  {i}: pos={p}, ori={o}")
    print("=================") """

print_cube(cubo,"")
girosv2.B(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"], cubo["aristas_ori"])
print_cube(cubo,"B")
girosv2.Bp(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"], cubo["aristas_ori"])
print_cube(cubo,"Bp")
""" girosv2.F(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"], cubo["aristas_ori"])
print_cube(cubo,"F")
girosv2.F(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"], cubo["aristas_ori"])
print_cube(cubo,"F") """
