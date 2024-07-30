nombre =  input("Ingrese su nombre ")
numero  = int(input("Ingrese un numero "))
contador = 0

for i in range (numero):
    contador += 1
    print (f"el numero es {contador}")

if nombre != "harold ":
    print("el nombre no es harold")

