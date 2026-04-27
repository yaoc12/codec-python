
''' 
    Reto de progamación simulador de probalidades de la ruleta rusa

    1.Descripcion del problema:
    se requeire desrrollar un progrma en python que simule un sistema de azar basado en un revolver de 6 recamaras. el programa debe gestionar eventos aleatorios, pausas de ejecucion para mejorar la experiencia de usiario y control del flujo basado en condiciones de victoria o derrota.

    2. requerimientos tecnicos 

    El algoritmo debe cumplir con los siguientes requisitos:

    * inicializacion: definir una recamara ganadora (bala) de forma aleatoria entre 1 y 6.  

    * bucle de juego : el usuario debe interactuar manualmente para girar el tambor y disparar.

    * Mecanica de azar: en cada turno, la posicion de la recamara que queda al frente al percutor debe ser aleatoria, simulando el giro del tambor.

    * Condicion de derrota: si la recamara selecionada coincide con la de la bala, el programa termina inmediatamente.

    * Condicion de victoria: el jugador gana si logra sobrevivir a 5 intentos (ya que el sexto seria el intento fatal). 

    '''
    
import random, time

    
print("="*50)
print("Bienvenido al juego de la ruleta rusa")
print("="*50)

input("Poner Bala en el Tambor (Presiona Enter)")
bala = random.randint(1,6)
time.sleep(0.5)     

    #variable para contar los disparos realizados
disparos = 0 

while True:
    input("Girar el Tambor (Presiona Enter)")
    recamara = random.randint(1,6)

    input("apuntar y disparar (Presiona Enter)")
    time.sleep(1)

    if recamara == bala:
        print("¡Bang! Has perdido. La bala estaba en la recamara", bala)
    
    else:
        disparos += 1
        print("Has sobrevivido a este intento.")
        print("Intentos sobrevividos:", disparos)

    if disparos == 5:
        print("¡Felicidades! Has ganado. Has sobrevivido a 5 intentos.")
        break


print("="*50)
print("Fin del juego. Gracias por jugar.")
print("="*50)