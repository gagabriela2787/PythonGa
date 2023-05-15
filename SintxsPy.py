#= para asignar una variable
#{} para designar bloques de codigo

'''x="el valor de (a+b)*c es"
a,b,c = 4,3,2
d = (a +b) * c
imprimir = True

if imprimir:
    print(x,d)

    # Salida: El valor de (a+b)*c es 14

x, y, z = 1, 2, 3

print (y)'''


import keyword
print(keyword.kwlist)

#no se pueden usar


#multiples lineas

x = 1 + 2 + 3 + 4 +\
    5 + 6 + 7 + 8

x = (1 + 2 + 3 + 4 +
    5 + 6 + 7 + 8)

#llamadas de funciones

def funcion (a,b,c):
    return a+b+c
d= funcion (10,23,3)
print(d)



#parentesis

x = 10
y = x*3-3**10-2+3

print(y)
x = 10
y = (x*3-3)**(10-2)+3
print(y)



#el alcance de las variables
#global y local

x = 10

def funcion():
    x = 5

funcion()
print(x)


'''#funcion print() separando por comas , los valores, es 
posible imprimir el texto y el contenido de variables.'''


x = 10
y = 20
z ="'Los valores x, y son:'"
print(z, x, y)

x = 10
y = 20
print("Los valores x, y son:", x, y)







