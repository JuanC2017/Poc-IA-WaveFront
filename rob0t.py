class Cola:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.insert(0,item)

    def desencolar(self):
        if self.estaVacia():
            return None
        else: return self.items.pop()

    def estaVacia(self):
        if len(self.items)==0:
            return True
        else: return False

    def tamano(self):
            return len(self.items)
cola=Cola()
ambiente= [["B","B","B","B","B","B","B"],
           ["B",0,0,0,0,0,"B"], #0
           ["B",0,0,-1,-1,0,"B"],#1
           ["B",0,0,0,-1,0,"B"],#2
           ["B",0,0,0,-1,0,"B"],#3
           ["B","B","B","B","B","B","B" ]]
              #0 #1 #2 #3 #4
              #(3,2)=1
              #(2,2) (4,2) (3,3) (3,1)
filas=4
columnas=5
listValues=[]
updateAmbiente=[]
conValue=0
x0=3+1 # coompenente en x de la coodenana final mas 1 ; para que sea la coomponente en la mattriz con pared
y0=4+1
x1=3+1
y1=2+1
coordenadas={}
for i in range(filas+2):
    for j in range(columnas+2):
        coordenadas.update({(i,j):ambiente[i][j]}) #Datos de la matriz corresponde dicionario con key de tuplas

def accion(func,i,j):
    return (func(i,j))

def abajo(i,j):

    i=i+1
    return (i,j)

def derecha(i,j):
    j=j+1
    return (i,j)

def arriba(i,j):
    i=i-1
    return(i,j)

def izquierda(i,j):
    j=j-1
    return(i,j)
#cooerdenadas[x0,y0]=1 #en la coordenada final inica con 1
#print(cooerdenadas[x,y])
"""estado=cooerdenadas.keys()
coordenada=[]
for i in estado:
    coordenada.append(i)
"""
#ambiente[x0][y0]=1
#print("cooerdenada en la matriz con pared",x0,y0)
#print(abajo(x,y),derecha(x,y),arriba(x,y),izquierda(x,y))
#print(type(abajo(x,y)))
vecinos=[izquierda,derecha,arriba,abajo] #lista de funciones de vecinos
def siguiente(x,y):
    while True:
        for moverse in vecinos:#Se mueve alos vecinos
            if (coordenadas.get(accion(moverse,x,y)))==0:
                cola.agregar(accion(moverse,x,y))#agrega ala cola los vecinos
                valueUtil=coordenadas[accion(moverse,x,y)]=coordenadas[x,y]+1
            if(coordenadas.get(accion(moverse,x,y))==coordenadas[x1,y1]):# si la coordenada final es igual ala inicial rompe
                break
        if(coordenadas.get(accion(moverse,x,y))==coordenadas[x1,y1]):# si la coordenada final es igual ala inicial rompe
            break
        if cola.tamano()==0:
            break
        else:
            #valueUtil+=1 #valor de utilidad ++
            nextStado=cola.desencolar()#saca el primer veicno que se visito
            x=nextStado[0] #estado siguente
            y=nextStado[1]
    print("R0botito Recorre hasta que el valor sea igual 1: ")
    while(valueUtil>=1):
        print(valueUtil)
        valueUtil-=1
coordenadas[x0,y0]=1
siguiente(x0,y0)
"""print(coordenada)
for i in ambiente:
    print(i)"""
print("Cola",cola.items)
value = coordenadas.values() #valores del diccionario
for i in value: #dicionario de valores a una nueva lista
    listValues.append(i)

for i in range(filas+2):
    updateAmbiente.append([])
    for j in range(columnas+2):#agregar ala fila i nueva columna con los datos de new
        updateAmbiente[i].append(listValues[conValue] if conValue<len(listValues) else None)
        conValue += 1

for i in updateAmbiente:
    print(i)
