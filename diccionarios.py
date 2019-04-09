diccionarios = {"HUEVOS": 22.50, "JAMON": 23} #Se crea un nuevo diccionario

print(diccionarios["HUEVOS"])

diccionarios.keys() #Keys devuelve UNICAMENTE las llaves
print("Las llaves del ccionario son: ", diccionarios.keys())

diccionarios.values() #Values devuelve UNICAMENTE valores
print("Los valores del diccionarios", diccionarios.values())

diccionarios.pop("HUEVOS") #Limitamos un elemento específico del diccionario
print(diccionarios)

diccionarios.update({"LECHE": 45}) #Agregamos o actualizamos un elemento del diccionario

print(diccionarios)
