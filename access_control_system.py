# le pedimos los datos al usuario 
nombre = input("porfavoor escribe aqui tu nombre     ")
edad = int(input("¿cuantos  años tienes?    "))

print(f"\n  datos guardados con exito!")

# paso 2: logica de decicion 
if edad >=18:
	                  # este bloque se ejecuta si la edad es igual o mayor a 18
	               print(f"\nbienvenido al club " + nombre + " ya eres mayor de edad.  ")
else: 	
      # este bloque se ejecuta si la condicion de arriba es falsa
 print(" lo siento, " + nombre + ". debes tener 18 años pa entrar ")                  