print ("Por favor, digite el número de alumnos")
n = int(input())
acum = 0
#ciclo for del rango
for i in range(0,n):
    print ("ingrese la nota") 
    nota = int(input())
    #suma acumulado + nota por cada alumno
    acum= acum + nota
#obtenemos el promedio
promedio = acum / n
print ("El promedio del salón es", promedio)