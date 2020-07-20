from time import sleep
import random
import sys
nivel = 1
puntaje=0
vidas=2
z=9
while z==9:
    #nivel: num -> num random
    #el juego me pedirá ingresar un nivel, y dependiendo del numero elegido comenzará a jugar con tal nivel
    #ejemplo: nivel(1): jugará bajo las condiciones del nivel 1, habrán por ejemplo 5 numeros que tendrá que memorizar el jugador
    def nivel (x):
        puntaje=0
        if x==1:
            vidas=2
            if vidas==0:
                sys.exit()
            n1 = random.randint (0,99)
            n2=random.randint (0,99)
            n3=random.randint (0,99)
            n4=random.randint (0,99)
            n5=random.randint(0,99)
            print "  " +str(n1)
            print "  " +str(n2)
            print "  " +str(n3)
            print "  " +str(n4)
            print "  " +str(n5)
            sleep (10)
            print 
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print"Han pasado 10 segundos"
            print "Ingrese el primer numero"
            numero1=input()
            if numero1!=n1:
                vidas= vidas-1
                print "Numero incorrecto!" 
            if numero1==n1:
                    puntaje = puntaje+10
            print "Ingrese numero 2"
            numero2= input()
            if numero2 !=n2:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero2==n2:
                    puntaje = puntaje +10
            print "Ingrese numero 3"
            numero3=input()
            if numero3 !=n3 :
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero3==n3:
                    puntaje =puntaje +10
            print "Ingrese numero 4"
            numero4=input()
            if numero4 !=n4:
                vidas =vidas-1
                print "Numero incorrecto!"
            if numero4==n4:
                    puntaje = puntaje +10
            print "Ingrese numero 5"
            numero5=input()
            if numero5 !=n5 :
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero5==n5:
                    puntaje = puntaje +10
            
            print "Puntaje Total Nivel 1:" +str(puntaje)
            return

        if x==2:
            vidas=2
            if vidas==0:
                sys.exit()
            n1=random.randint (0,99)
            n2=random.randint (0,99)
            n3=random.randint (0,99)
            n4=random.randint (0,99)
            n5=random.randint (0,99)
            n6=random.randint (0,99)
            n7=random.randint (0,99)
            print "  " +str(n1)
            print "  " +str(n2)
            print "  " +str(n3)
            print "  " +str(n4)
            print "  " +str(n5)
            print "  " +str(n6)
            print "  " +str(n7)
            sleep (10)
            print 
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print "Han pasado 10 segundos"
            print "Ingrese numero 1"
            numero1=input()
            if numero1 !=n1:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero1==n1:
                    puntaje = puntaje+10
            print "Ingrese numero 2"
            numero2=input()
            if numero2 !=n2:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero2==n2:
                    puntaje = puntaje+10
            print "Ingrese numero 3"
            numero3=input()
            if numero3 !=n3:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero3==n3:
                    puntaje = puntaje+10
            print "Ingrese numero 4"
            numero4=input()
            if numero4 != n4:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero4==n4:
                    puntaje = puntaje+10
            print "Ingrese numero 5"
            numero5=input()
            if numero5 !=n5:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero5==n5:
                    puntaje = puntaje+10
            print "Ingrese numero 6"
            numero6=input()
            if numero6 !=n6:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero6==n6:
                    puntaje = puntaje+10
            print "Ingrese numero7"
            numero7=input()
            if numero7 !=n7:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero7==n7:
                    puntaje = puntaje+10
            if vidas==0:
                sys.exit()
            print "Puntaje Total Nivel 2:" +str(puntaje)
            return

        if x==3:
            vidas=2
            if vidas==0:
                sys.exit()
            n1=random.randint (10,9999)
            n2=random.randint (10,9999)
            n3=random.randint (10,9999)
            n4=random.randint (10,9999)
            n5=random.randint (10,9999)
            n6=random.randint (10,9999)
            n7=random.randint (10,9999)
            n8=random.randint (10,9999)
            n9=random.randint (10,9999)
            print "  " +str(n1)
            print "  " +str(n2)
            print "  " +str(n3)
            print "  " +str(n4)
            print "  " +str(n5)
            print "  " +str(n6)
            print "  " +str(n7)
            print "  " +str(n8)
            print "  " +str (n9)
            sleep (10)
            print 
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print "Han pasado 10 segundos"
            print "Ingrese numero 1"
            numero1=input()
            if numero1 !=n1:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero1==n1:
                    puntaje = puntaje+10
            print "Ingrese numero2"
            numero2=input()
            if numero2 !=n2:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero2==n2:
                    puntaje = puntaje+10
            print "Ingrese numero 3"
            numero3=input()
            if numero3 !=n3:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero3==n3:
                    puntaje = puntaje+10
            print "Ingrese numero 4"
            numero4=input()
            if numero4 !=n4:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero4==n4:
                    puntaje = puntaje+10
            print "Ingrese numero 5"
            numero5=input()
            if numero5 !=n5:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero5==n5:
                    puntaje = puntaje+10
            print "Ingrese numero 6"
            numero6=input()
            if numero6 !=n6:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero6==n6:
                    puntaje = puntaje+10
            print "Ingrese numero 7"
            numero7=input()
            if numero7 !=n7:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero7==n7:
                    puntaje = puntaje+10
            print "Ingrese numero 8"
            numero8=input()
            if numero8 != n8:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero8==n8:
                    puntaje = puntaje+10
            print "Ingrese numero 9"
            numero9=input()
            if numero9 !=n9:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero9==n9:
                    puntaje = puntaje+10
            
            print "Puntaje Total Nivel 3:" +str(puntaje)
            return

        if x==4:
            vidas=2
            if vidas==0:
                sys.exit()
            n1=random.randint (10,9999)
            n2=random.randint (10,9999)
            n3=random.randint (10,9999)
            n4=random.randint (10,9999)
            n5=random.randint (10,9999)
            n6=random.randint (10,9999)
            n7=random.randint (10,9999)
            n8=random.randint (10,9999)
            n9=random.randint (10,9999)
            n10=random.randint (10,9999)
            n11=random.randint (10,9999)
            print "  " +str(n1)
            print "  " +str(n2)
            print "  " +str(n3)
            print "  " +str(n4)
            print "  " +str(n5)
            print "  " +str(n6)
            print "  " +str(n7)
            print "  " +str(n8)
            print "  " +str(n9)
            print "  " +str(n10)
            print "  " +str(n11)
            sleep (10)
            print 
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print"Han pasado 10 segundos"
            print "Ingrese numero 1"
            numero1=input()
            if numero1 !=n1:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero1==n1:
                    puntaje = puntaje+10
            print "Ingrese numero2"
            numero2=input()
            if numero2 !=n2:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero2==n2:
                    puntaje = puntaje+10
            print "Ingrese numero 3"
            numero3=input()
            if numero3 !=n3:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero3==n3:
                    puntaje = puntaje+10
            print "Ingrese numero 4"
            numero4=input()
            if numero4 !=n4:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero4==n4:
                    puntaje = puntaje+10
            print "Ingrese numero 5"
            numero5=input()
            if numero5 !=n5:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero5==n5:
                    puntaje = puntaje+10
            print "Ingrese numero 6"
            numero6=input()
            if numero6 !=n6:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero6==n6:
                    puntaje = puntaje+10
            print "Ingrese numero 7"
            numero7=input()
            if numero7 != n7:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero7==n7:
                    puntaje = puntaje+10
            print "Ingrese numero 8"
            numero8=input()
            if numero8 !=n8:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero8==n8:
                    puntaje = puntaje+10
            print "Ingrese numero 9"
            numero9=input()
            if numero9 !=n9:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero9==n9:
                    puntaje = puntaje+10
            print "Ingrese numero 10"
            numero10=input()
            if numero10 !=n10:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero10==n10:
                    puntaje = puntaje+10
            print "Ingrese numero 11"
            numero11=input()
            if numero11 !=n11:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero11==n11:
                    puntaje = puntaje+10
        
            print "Puntaje Total Nivel 4:" +str(puntaje)
            return

        if x==5:
            vidas=2
            if vidas==0:
                sys.exit()
            n1=random.randint (100,999999)
            n2=random.randint (100,999999)
            n3=random.randint (100,999999)
            n4=random.randint (100,999999)
            n5=random.randint (100,999999)
            n6=random.randint (100,999999)
            n7=random.randint (100,999999)
            n8=random.randint (100,999999)
            n9=random.randint (100,999999)
            n10=random.randint (100,999999)
            n11=random.randint (100,999999)
            n12=random.randint (100,999999)
            n13=random.randint (100,999999)
            n14=random.randint (100,999999)
            print "  " +str(n1)
            print "  " +str(n2)
            print "  " +str(n3)
            print "  " +str(n4)
            print "  " +str(n5)
            print "  " +str(n6)
            print "  " +str(n7)
            print "  " +str(n8)
            print "  " +str(n9)
            print "  " +str(n10)
            print "  " +str(n11)
            print "  " +str(n12)
            print "  " +str(n13)
            print "  " +str(n14)
            sleep (10)
            print 
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print
            print "Han pasado 10 segundos"
            print "Ingrese numero 1"
            numero1=input()
            if numero1 !=n1:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero1==n1:
                    puntaje = puntaje+10
            print "Ingrese numero2"
            numero2=input()
            if numero2 !=n2:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero2==n2:
                    puntaje = puntaje+10
            print "Ingrese numero 3"
            numero3=input()
            if numero3 !=n3:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero3==n3:
                    puntaje = puntaje+10
            print "Ingrese numero 4"
            numero4=input()
            if numero4 !=n4:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero4==n4:
                    puntaje = puntaje+10
            print "Ingrese numero 5"
            numero5=input()
            if numero5 !=n5:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero5==n5:
                    puntaje = puntaje+10
            print "Ingrese numero 6"
            numero6=input()
            if numero6 !=n6:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero6==n6:
                    puntaje = puntaje+10
            print "Ingrese numero 7"
            numero7=input()
            if numero7 !=n7:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero7==n7:
                    puntaje = puntaje+10
            print "Ingrese numero 8"
            numero8=input()
            if numero8 !=n8:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero8==n8:
                    puntaje = puntaje+10
            print "Ingrese numero 9"
            numero9=input()
            if numero9 !=n9:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero9==n9:
                    puntaje = puntaje+10
            print "Ingrese numero 10"
            numero10=input()
            if numero10 !=n10:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero10==n10:
                    puntaje = puntaje+10
            print "Ingrese numero 11"
            numero11=input()
            if numero11 !=n11:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero11==n11:
                    puntaje = puntaje+10
            print "Ingrese numero 12"
            numero12=input()
            if numero12 !=n12:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero12==n12:
                    puntaje = puntaje+10
            print "Ingrese numero 13"
            numero13=input()
            if numero13 != n13:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero13==n13:
                    puntaje = puntaje+10
            print "Ingrese numero 14"
            numero14=input()
            if numero14 !=n14:
                vidas=vidas-1
                print "Numero incorrecto!"
            if numero14==n14:
                    puntaje = puntaje+10
           
            print "Puntaje Total Nivel 5:" +str(puntaje)
            return
        return
    #juego: num -> funcion nivel
    #juego valida si la opcion elegida, en este caso el numero es acorde con algun nivel
    #ejemplo: juego (9): debería devolver opcion no valida, ya que no existe tal nivel
    #ejemplo:juego (2): debería devolver nivel 2
    def juego (x):
        x=input("Ingrese nivel")
        if x<=1 or x>=5:
                print "Opcion no valida"
        if x==1:
            return nivel(1)
        elif x==2:
            return nivel(2)
        elif x==3:
            return nivel(3)
        elif x==4:
            return nivel(4)
        elif x==5:
            return nivel(5)
        return

    
    mayorPuntaje= max(str(puntaje))
    print "-----------------Menu Principal memo game-------------------"
    print "1.elegir nivel"
    print"2.iniciar juego "
    print"3.Salir"
    print "Dificultad actual:"+str(nivel), "/ 5"
    print "Mayor puntaje alcanzado:" , str(mayorPuntaje)
    opcionParaIniciar= input("Ingrese opcion:")
    if opcionParaIniciar==3:
        print "Fin del juego"
        sys.exit ()
    if opcionParaIniciar==1:
        x=input("Ingrese nivel:")
        if x<1 or x>5:
                print "Opcion no válida"
        if x==1:
            nivel (x)
        if x==2:
            nivel (x)
        if x==3:
            nivel (x)
        if x==4:
            nivel (x)
        if x==5:
            nivel (x)
    if opcionParaIniciar==2:
        print "Comenzara el juego en 3 segundos, atento"
        sleep (3)
        nivel(1)
            

