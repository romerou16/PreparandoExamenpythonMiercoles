#COMENTARIO DE LINEA

'''
COMENTARIO DE BLOQUE
'''

#declarando datos primitivos
nombreUsuario="Andrea"
edadUsuario=34
estaturaUsuario=1.63
estaLloviendo=True

#mostrar informacion en pantalla
print(f"su nombre es: {nombreUsuario}")
print(f"su edad es: {edadUsuario}")
print(f"apreciado: {nombreUsuario} su estatura es {estaturaUsuario}")

#DESEO RECOLECTAR DATOS DESDE EL USUARIO
direccionUsuario=input("Digite su direccion: ")
print(f"su direccion es: {direccionUsuario}")

salarioUsuario=int(input("Digite salario: "))
bonoMensualUsuario=int(input("Digite el valor del bono: "))

salarioIntegral=salarioUsuario+bonoMensualUsuario
print(salarioIntegral)
