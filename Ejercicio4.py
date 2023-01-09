#Pregunta input por cada asistente
Curry = input ("¿Stephen Curry asistio a la boda de Adrian? si/no: ")
Jordan = input ("¿Michael Jordan asistio a la boda de Adrian? si/no: ")
Morant = input ("¿Ja Morant asistio a la boda de Adrian? si/no: ")

 
#Condicional while si las respuestas de los 3 son "si"
if Curry == "si" and Jordan == "si" and Morant == "si":
  print("Asistieron las 3 estrellas")
# O si no, que imprima que no asistieron los 3
else:
  print("No asistieron los 3")