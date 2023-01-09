#Entrada y declaración de variable
print("Bienvenido a la Empresa SolGas")
a=int(input("Ingrese el salario que recibe: "))
#Proceso
if a<1500:
    b=1.10*a
    print("Usted recibirá ahora:",b)
else:
    print("Usted mantendrá su salario:",a)