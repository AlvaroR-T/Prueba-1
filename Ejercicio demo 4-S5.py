#Entrada
C1=int(input("Ingrese su salario #1: "))
C2=int(input("Ingrese su salario #2: "))
C3=int(input("Ingrese su salario #3: "))
if C1<=C3 and C2<=C3:
    mayor=C3
elif C1<=C2 and C3<=C2:
    mayor=C3
else:
    mayor=C1

if C1<=C2 and C1<=C3:
    menor=C1
elif C2<=C1 and C2<=C3:
    menor=C2
else:
    menor=C3

#Salida:
print("El dispondrá de comprar la nueva televisión y de salario más alto es:", mayor)
print("El dispondrá de comprar los menús y de menor salario es:", menor)