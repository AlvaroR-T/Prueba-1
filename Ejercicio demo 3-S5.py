#Entrada
print("Muy buenos días,estimado")
a=int(input("Ingrese su edad:"))
#Proceso
if a>0 and a<18:
    print("Usted es menor de edad")
elif a>=18 and a<60:
    print("Usted es un adulto")
elif a>=60 and a<100:
    print("Usted una adulto mayor")
else:
    print("Usted es una persona longeva")