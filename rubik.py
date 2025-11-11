import girosv2
from collections import deque
cubo_resuelto = {
        "esquinas_pos": [0,1,2,3,4,5,6,7],
        "esquinas_ori": [0,0,0,0,0,0,0,0],
        "aristas_pos": [0,1,2,3,4,5,6,7,8,9,10,11],
        "aristas_ori": [0,0,0,0,0,0,0,0,0,0,0,0]
    }

class Nodo:
    def __init__(self, cubo, movimiento=None, padre=None, profundidad=0):
        self.cubo = cubo                
        self.movimiento = movimiento    
        self.padre = padre              
        self.profundidad = profundidad  

    def __repr__(self):
        return f"Nodo({self.movimiento}, prof={self.profundidad})"

def movimientosPosibles(ultimo_Giro=None):
     todos = ["U", "Up", "U2",
              "R", "Rp", "R2",
              "F", "Fp", "F2",
              "L", "Lp", "L2",
              "D", "Dp", "D2",
              "B", "Bp", "B2"]
     if ultimo_Giro is None:
         return todos
     grupo = todos.index(ultimo_Giro)//3
     return todos[:grupo*3]+ todos[(grupo*3+3):]    

def generar_hijos(padre):
    hijos=[]
    for m in movimientosPosibles(padre.movimiento):
        nuevo_cubo=(getattr(girosv2,m)(padre.cubo["esquinas_pos"],padre.cubo["esquinas_ori"],padre.cubo["aristas_pos"], padre.cubo["aristas_ori"]))
        hijo = Nodo(
            cubo=nuevo_cubo,
            movimiento=m,
            padre=padre,
            profundidad=padre.profundidad + 1
        )
        hijos.append(hijo)
    return hijos

def main():
    padre = Nodo(cubo_resuelto)
    hijos = generar_hijos(padre)
    for h in hijos:
        print(h.movimiento)
     
def print_cube(cubo, giro):
    print("=== ",giro," ===")
    print("Esquinas:")
    for i, (p, o) in enumerate(zip(cubo["esquinas_pos"],cubo["esquinas_ori"])):
        print(f"  {i}: pos={p}, ori={o}")
    print("\nAristas:")
    for i, (p, o) in enumerate(zip(cubo["aristas_pos"], cubo["aristas_ori"])):
        print(f"  {i}: pos={p}, ori={o}")
    print("=================") 
main()
""" 
print_cube(cubo,"")
getattr(girosv2,"B")(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"], cubo["aristas_ori"])
print_cube(cubo,"B")
girosv2.Bp(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"], cubo["aristas_ori"])
print_cube(cubo,"Bp")
girosv2.F(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"], cubo["aristas_ori"])
print_cube(cubo,"F")
girosv2.F(cubo["esquinas_pos"],cubo["esquinas_ori"],cubo["aristas_pos"], cubo["aristas_ori"])
print_cube(cubo,"F") """
