from random import randint

num_magico   = randint (1,1000)
num_intentos = 10

while (num_intentos > 0):
    num_usuario = input ("Ingrese numero:")
    if (num_usuario == num_magico):
        print ("Felicitaciones")
        exit (0)
    else:
        num_intentos -= 1
        if (num_magico > num_usuario):
            print ("Es mayor")
        else:
            print ("Es menor")
        #finIf
    #finIf

#FinWhile

if (num_intentos == 0):
    print ("Perdiste el numero fue:", num_magico)
#finIf

