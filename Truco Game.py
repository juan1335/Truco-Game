import random
cartas = (1,2,3,4,5,6,7,8,9,10,11,12,13)
palos = ("diamante", "pica", "trebol", "corazon" )
nombre = input("Ingrese su nombre: ")

ganadas = pozo_ini = max = black_jacks = ganadas_cupri = empates = cantidad_apuestas = apuestas_total = 0
actual_racha = conteo_racha_cupri = cantidad_perdida = max_perdida = 0
pozo_max = anterior_cupri = perdidas = False
pozo = -1

while pozo < 1 or pozo > 100000:
    pozo = int(input("Ingrese el monto inicial del pozo (no mayor a $100000): "))
    if pozo < 1 or pozo > 100000:
        print("⚠ ERROR ⚠, ingrese un monto no mayor a $100000 y menor a $1 ")

def valor_especiales(cart):
    if cart == 11 or cart == 12 or cart == 13:
        cart = 10
    else:
        cart = cart
    return cart

def carta(c):
    if c == 1:
        carta_n = "AS"
    elif c == 11:
        carta_n = "J"
    elif c == 12:
        carta_n = "Q"
    elif c == 13:
        carta_n = "K"
    else:
        carta_n = c

    return carta_n

def ases(carta, resultado):
    if carta == 11 and resultado > 21:
        resultado = resultado - carta
        carta = 1
        resultado = resultado + carta
    return carta, resultado


op = 1
while op != 3:
    parar = False
    segunda_carta = False
    bj = False
    bj_cupri = False
    un_as = un_as_cupri = False
    tu_resultado = su_resultado = ant_cn = ant_cn_cupri = 0

    if pozo_max == False:
        max = pozo
        pozo_max = True
    else:
        if pozo > max:
            max = pozo

    print("Tu pozo actual es de:",pozo)

    print("=========Menu de opciones=========")
    print("1- Apostar")
    print("2- Jugar una mano")
    print("3- Salir")
    print("==================================")

    op = int(input("Ingrese el numero de la opcion que desea seguir: "))
    if op == 1:
        print("Tu pozo es de:", pozo)
        sumar = int(input("Ingrese suma del monto: "))
        if sumar > 0:
            pozo = pozo + sumar
            if pozo > 100000:
                pozo = pozo - sumar
                print("⚠ No se pudo sumar, el pozo no puede superar a 100000 ⚠")
        else:
            print("⚠ No se pudo sumar, ingrese un numero mayor a 0 ⚠")
    elif op == 2:

        if pozo >= 5:
            print("Buenos dias", nombre, "ha elegido la opcion 2 (Consejo: Apueste con moderacion, el casino no se hace responsable de que tenga que vender su casa) ")
            apostar = int(input("Ingrese monto de apuesta (tiene que ser multiplo de 5) :"))
            if apostar > 0 and apostar % 5 == 0 and apostar <= pozo:
                print("Se cargo la apuesta correctamente")
                apuestas_total += apostar
                cantidad_apuestas += 1
                pozo_ini = pozo
            else:
                apostar = 0
                print("⚠ No se cargo correctamente la apuesta ⚠")
                continue
        else:
            print("⚠ No tenes suficiente plata en el pozo ⚠")
            continue

        pozo = pozo - apostar

        c1 = random.choice(cartas)
        c1_cupri = random.choice(cartas)
        p1 = random.choice(palos)
        p1_cupri = random.choice(palos)
        c2 = random.choice(cartas)
        p2 = random.choice(palos)

        cart_1 = carta(c1)
        c1 = valor_especiales(c1)
        cart_2 = carta(c2)
        c2 = valor_especiales(c2)

        cart_cupri_1 = carta(c1_cupri)
        c1_cupri = valor_especiales(c1_cupri)

        if c1 == 1:
            c1 = 11

        tu_resultado = c1 + c2

        if c2 == 1:
            tu_resultado = tu_resultado - c2
            if tu_resultado <= 10:
               c2 = 11
            tu_resultado = c1 + c2


        if c1_cupri == 1:
            c1_cupri = 11
        print("---------------------------------------------")
        print("♠♢Te toco la carta de", cart_1, "de", p1,"♣♥")
        print("♠♢Te toco la carta de", cart_2, "de", p2,"♣♥")
        print("")
        cant_cartas = 2
        print("♠♢Al cuprier le toco la carta de", cart_cupri_1, "de", p1_cupri,"♣♥")
        cant_cartas_cupri = 1

        while tu_resultado < 21 and parar == False:
            print("")
            print("tu resultado es igual a", tu_resultado)
            print("")
            print("Tu monto de la apuesta es de: ", apostar)
            seguir = int(input("¿Desea levantar otra carta? (1 para si - 0 para no): "))
            if seguir == 1:

                cant_cartas += 1
                cn = random.choice(cartas)
                pn = random.choice(palos)
                cart_n = carta(cn)
                cn = valor_especiales(cn)

                tu_resultado += cn

                if cn == 1:
                    tu_resultado = tu_resultado - cn
                    if tu_resultado <= 10:
                        cn = 11
                    tu_resultado += cn

                c1, tu_resultado = ases(c1,tu_resultado)
                c2, tu_resultado = ases(c2,tu_resultado)

                if un_as == True and tu_resultado > 21:
                   tu_resultado = tu_resultado - 10
                   un_as = False

                if cn == 11:
                   un_as = True


                print("")
                print("♠♢Te toco la carta de", cart_n, "de", pn,"♣♥")

            elif seguir == 0:
                parar = True
            else:
                print("")
                print("No eligio ninguna opcion de las pedidas, finaliza su turno.")
                parar = True
        else:
            if cant_cartas == 2 and tu_resultado == 21:
                print("-----------------------------------------------------")
                print("Tuviste un blackJack natural, no levantas mas cartas.")
                print("-----------------------------------------------------")
                bj = True
            else:
                print("")
                print("Tu resultado es igual a", tu_resultado, ",no levantas mas cartas.")
        print("")
        print("♠♢La primera carta del cuprier había sido de", cart_cupri_1, "de", p1_cupri,"♣♥")

        while su_resultado <= 16:
            cant_cartas_cupri += 1
            cn_cupri = random.choice(cartas)
            pn_cupri = random.choice(palos)
            cart_cupri_n = carta(cn_cupri)
            cn_cupri = valor_especiales(cn_cupri)

            if segunda_carta == False:
                su_resultado = c1_cupri + cn_cupri
                segunda_carta = True
            else:
                su_resultado += cn_cupri


            if cn_cupri == 1:
                su_resultado = su_resultado - cn_cupri
                if su_resultado <= 10:
                    cn_cupri = 11
                su_resultado += cn_cupri

            c1_cupri, su_resultado = ases(c1_cupri,su_resultado)

            if un_as_cupri == True and su_resultado > 21:
               su_resultado = su_resultado - 10
               un_as_cupri = False

            if cn_cupri == 11:
               un_as_cupri = True


            print("")
            print("♠♢Al cuprier le toco la carta de", cart_cupri_n, "de", pn_cupri,"♣♥")
        else:
            if cant_cartas_cupri == 2 and su_resultado == 21:
                print("------------------------------------------------------------")
                print("El cuprier tuvo un BlackJack natural, no levanta mas cartas.")
                print("------------------------------------------------------------")
                bj_cupri = True
            print("")
            print("El cuprier se plantó, su total acumulado es de", su_resultado)
            print("")

        print("Monto inicial del pozo: ",pozo_ini)
        print("Monto de la apuesta: ", apostar)

        if (tu_resultado == 21 and bj == True) or (su_resultado and bj_cupri == True):
            black_jacks += 1

        if bj:
            if bj_cupri:
                print("----------------------------------------------")
                print("Empataste con el cuprier con BlackJack natural")
                print("----------------------------------------------")
                empates += 1
            else:
                print("-----------------------------")
                print("Ganaste por BlackJack natural")
                print("-----------------------------")
                apostar = apostar * 2
                ganadas += 1
        elif bj_cupri:
            print("-------------------------------------")
            print("Gano el cuprier con BlackJack natural")
            print("-------------------------------------")
            cantidad_perdida = apostar/2
            apostar = apostar / 2
            ganadas_cupri += 1
        elif tu_resultado > 21:
            print("------------------------------")
            print("⚠ Te pasaste de 21, perdiste ⚠")
            print("------------------------------")
            cantidad_perdida = apostar/2
            apostar = apostar / 2
            ganadas_cupri += 1
        elif tu_resultado == su_resultado:
            print("------------------------")
            print("Empataste con el cuprier")
            print("------------------------")
            empates += 1
        elif tu_resultado == 21:
            print("------------------")
            print("Ganaste al cuprier")
            print("------------------")
            apostar = apostar * 2
            ganadas += 1
        elif su_resultado == 21:
             print("--------------------------")
             print("Perdiste contra el cuprier")
             print("--------------------------")
             cantidad_perdida = apostar/2
             apostar = apostar/2
             ganadas_cupri += 1
        elif tu_resultado < 21:
            if su_resultado < 21:
                if tu_resultado < su_resultado:
                    print("--------------------------")
                    print("Perdiste contra el cuprier")
                    print("--------------------------")
                    cantidad_perdida = apostar/2
                    apostar = apostar/2
                    ganadas_cupri += 1
                else:
                    print("------------------")
                    print("Ganaste al cuprier")
                    print("------------------")
                    apostar = apostar * 2
                    ganadas += 1
            else:
                print("------------------")
                print("Ganaste al cuprier")
                print("------------------")
                apostar = apostar * 2
                ganadas += 1


        if anterior_cupri == False and ganadas_cupri > 0:
            actual_racha = ganadas_cupri
            conteo_racha_cupri = 1
            anterior_cupri = True
        else:
            if actual_racha < ganadas_cupri:
                conteo_racha_cupri += 1
            else:
                conteo_racha_cupri = 0

        if actual_racha < conteo_racha_cupri:
            actual_racha = conteo_racha_cupri

        if perdidas == False:
           max_perdida = cantidad_perdida
           perdidas = True
        else:
            if cantidad_perdida > max_perdida:
               max_perdida = cantidad_perdida


        pozo = pozo + apostar


    elif op == 3:
        break
    else:
        print("")
        print("⚠ ERROR ⚠, presione un numero dentro de las opciones: ")

partidas = ganadas + ganadas_cupri + empates
porcentaje_jugador = ganadas*100/partidas
promedio = apuestas_total/cantidad_apuestas
print("=======================ESTADISTICAS FINALES==================")
print("El porcentaje de victorias del jugador :",int(porcentaje_jugador),"%")
print("La racha mas larga de victorias del croupier fue de:",actual_racha)
print("La cantidad de manos donde hubo un blackjack natural es igual a: ",black_jacks)
print("El pozo maximo que llego a tener el jugador fue de:", max)
print("El monto promedio del que dispuso el jugador para realizar apuestas fue de:", int(promedio))
print("La perdida mas grande del jugador fue de:", int(max_perdida))
print("==============================================================")
