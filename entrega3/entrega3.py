import sys

def calcular_sillas_y_tiempo(cantidad_invitados, momentos):
    """
    eventos = [(0,0)]*cantidad_invitados
    print(eventos)
    for i in range(cantidad_invitados):
        llegada,salida = momentos[i]
        eventos[i] = (llegada,1)
        eventos[i+1] = (salida,-1)

    print(eventos)
    """
    eventos = []
    # Construir la lista de eventos
    for i in range(cantidad_invitados):
        llegada, salida = momentos[i]
        eventos.append((llegada, 1))  # 1 representa la llegada
        eventos.append((salida, -1))  # -1 representa la salida


    # Ordenar eventos por tiempo
    eventos.sort()
    

    sillas_ocupadas = 0
    sillas_necesarias = 0
    tiempo_ocupacion_maximo = 0
    tiempo_anterior = 0

    for tiempo, tipo in eventos:
        if tipo == 1:  # Llegada
            sillas_ocupadas += 1
            sillas_necesarias = max(sillas_necesarias, sillas_ocupadas)
    
        else:  # Salida
            #cuando se va la persona y las sillas necesarias == ocupadas, quiere decir que cuando el estaba
            #las sillas estaban todas ocupadas y al levantarse ya no lo estarán
            
            if sillas_necesarias == sillas_ocupadas:
                tiempo_ocupacion_maximo = tiempo - tiempo_anterior
            

            if sillas_necesarias <sillas_ocupadas:
                tiempo_ocupacion_maximo = 0
        
            sillas_ocupadas -= 1
            
        tiempo_anterior = tiempo
    print(sillas_necesarias, tiempo_ocupacion_maximo)

# Ejemplo de uso
nombre_fichero = 'input_01.txt'
sys.stdin = open(nombre_fichero, "r")

# Leer el número de casos
t = int(sys.stdin.readline().strip())

for _ in range(t):
    # Leer el número de invitados (n) y el valor x
    n=int(sys.stdin.readline().strip())

    # Leer las llegadas y salidas de los invitados
    momentos = []
    for _ in range(n):
        entrada = sys.stdin.readline().split()
        llegada, salida = map(int, entrada)
        momentos.append((llegada, salida))

    # Calcular y imprimir la solución para el caso actual
    solucion = calcular_sillas_y_tiempo(n, momentos)


