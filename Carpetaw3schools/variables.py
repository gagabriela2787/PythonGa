x, y ,z = 5, "john", 3.33
print(type(x))
print(type(y))
print(type(z))
# con la  funcion "type()" 
# se puede obtener el tipo de datos de la variable
#se pueden asignar varias variables en una linea

a = "valteri"
A= "valteri"
print(a,A)


#sensible a las minusculas y mayusculas



b = c = d = "Orange"
print(b)
print(c)
print(d)


#se pueden asignar un valor a varias variables


verduras = ["acelga", "berenjena","lechuga"]

e,f,g = verduras
print(e)
print(f)
print(g)

#se puede extraer los valores en variables de una lista o tupla



h = "python"
i= "es"
j= "genial"

print(h,i,j)
print(h+i+j)

k=10
l="valte"
print(k,l)

k=10
l=5
print(k+l)


#lo anterior son variables globales,
#se usan fuera y adentro de las funciones



x ="fantastico" #variable con el mismo nombre

def myfunc():
    x = "facil" #variable con el mismo nombre
    print("python is" ,  x) #se imprime

myfunc()

print("python is" , x)#se imprime


#si se crea una variable dentro de una funcion, esa variable 
#solo se usará dentro de esa funcion
#para crear una  variable dentro de una  funcion y que sea
#global se debe usar la keyword 'global'


def myfunc():
    global x
    x ="rapido"
myfunc()

print("python is" , x)









