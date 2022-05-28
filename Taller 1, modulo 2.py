#Taller 1
#Dime lo que sabes 
#Gariela Torres
#ID:1001970935
#ID:502193
#correo:gabriela.torresr@correo.upb.edu.co
#Cel:3234708201
#Diplomado de PYTHON APLICADO A LA INGENIERIA 
#Docente:Roberto Paez Salgado
#Modulo 2

#Defino las variables de mi ecuacion como parametros de una Funcion 
def ecuacion1(a,b,c,d,e,f):
#Defino la operacion y retorno a mi funcion 
    return ((a+(b/c))/(d+(e/f)))
#Llamo a mi funcion y asigno lo  valores de las  variables como argumentos
ecu1 = ecuacion1(100,200,300,400,500,600)
#imprimo la ecuacion 1
print("ecu1",ecu1)

#Defino las variables de mi ecuacion como parametros de una Funcion
def ecuacion2(a,b,c,d):
#Defino la operacion y retorno a mi funcion
    return (a-(b/(c-d)))
#Llamo a mi funcion y asigno lo  valores de las  variables como argumentos
ecu2 = ecuacion2(100,200,300,400)
#imprimo la ecuacion 2
print("ecu2",ecu2)

#realizo una reasignacion de valores a mis variables (intercambio los valores)
ecu1,ecu2 = ecu2,ecu1

#imprimo el resultado con sus nuevos valores
print(ecu1)
print(ecu2)