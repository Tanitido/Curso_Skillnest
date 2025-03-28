nombre = "esteban"
apellido = "quintero"
completo = nombre+" "+apellido  # concatenacion manual
# concatenacion con f-string , { se hace con alt+123
opcion2 = f"{nombre} {apellido}"
# concatenacion con f-string que muestra que se pueden hacer operaciones
opcion3 = f"{nombre[0]} {apellido[0:3]} {5-9}"
print(completo)
print(opcion2)
print(opcion3)
