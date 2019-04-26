from funciones.funciones44 import consecutivo

listab = []
cantid = int(input("Digite la cantidad de valores que va a ingresar:"))
for i in range(cantid):
 val = int(input("Ingrese los valores:"))
 listab.append(val)

x = consecutivo(listab)
print(x)