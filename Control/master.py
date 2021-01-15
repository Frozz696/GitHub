from Control.personajes import *

import random
import sys
import textwrap

ancho_linea = 72
linea_punteada = ancho_linea * '-'
jugador = {
    "arma": 1,
    "casco": 0,
    "armadura": 0,
    "escudo": 2,
    "brazal": 0,
    "grbas": 0,
    "botas": 0,
    "pocion": 0,
    "item": 0,
    "nombre": "aventurero"
}


def crea_enemigo():
    enemigo = random.randint(1, 4)
    if enemigo == 1:
        print(combate(jugador, Rata()))

    if enemigo == 3:
        print(combate(jugador, Goblin()))


def camino():
    crea_enemigo()
    print(
        "Mirando a tu alrededor puedes ver que el resto de la sala esta vacio, pero hay dos pasadizo que salen"
    )
    print("de la habitacion y se adentran más profundamente en el dungeon")
    direc = input("(pasadizos oriental/pasadizo occidental) :")
    if direc == "pasadizo oriental":
        pasillo_oriental()

    elif direc == "pasadizo occidental":
        pasillo_occidental()


def atributos():
    print("Tu nombre es :", jugador.nombre)
    print("Tus puntos de vida son :", jugador.puntos_golpe)
    print("Tu raza es :", jugador.raza)
    print("Tu clase es :", jugador.clase)
    print("Tu nivel es :", jugador.nivel)
    print(linea_punteada)


def atributosLVL(jlA):
    print("Tus puntos de vida son :", jugador.puntos_golpe + 2)
    print("Tu defensa :", jugador.defensa + 1)
    print("Tu fuerza es :", jugador.atkcuerpoAcuerpo + 1)
    print("Tu nivel es :", jugador.nivel + 1)
    print("Tu agilidad es :", jugador.agilidad + 1)


def comprobar_lvl(jl):
    if jugador.xp > jugador.xpSiguientelvl:
        jugador.xp = 0
        print("Tus fuerzas aumentan!")
        print(linea_punteada)
        atributosLVL(jugador)
        print(linea_punteada)


def cerradura():
    if (jugador.mente + jugador.dextresa) < random.randint(1, 8):
        print("Logras forzar la ceradura")
        print(linea_punteada)
    else:
        print("La cerradura se encuentra fuertemente cerrada")
        print(linea_punteada)


def conocimiento_buscar_percepcion():
    if (jugador.mente + jugador.intelecto) < random.randint(1, 8):
        print("Logras recordar")
        print(linea_punteada)
    else:
        print("Tu mente esta vacia")
        print(linea_punteada)


def sala_jefe():
    print(
        "el pasadizo termina en una enome sala con el techo abovedado. Las escaleras del otro lado de la habitación"
    )
    print(
        "suben hasta una plataforma, encima de la cual se alza un trono dorado decorado con diamantes y rubies brillantes."
    )
    print(
        "En el trono se sienta un esqueleto vestido con armadura de un rey, vieja y oxidad, provisto de una espada larga"
    )
    print("que brilla estrañamente en sus huesudas manos")
    print(
        "La cabeza del esqueleto se gira extrañamente hacia ti, con sus orbitas vacias encendiendose con llasmas rojas"
    )
    print(
        "Su mandivula se abre en una sonrisa horrible mientras levanta la espada largas y te señala con ella."
    )
    if jugador.evento == 0:
        print(
            "Aferrando la espada larga de tu padre, avanzas hacia el esqueleto "
        )
        print(combate(jugador, Esqueleto()))
        if jugador.puntos_golpe <= 0:
            print("Ganaste!!!!")
            jugador.dinero += 50
            jugador.xp = random.randint(20, 30)

    if jugador.evento == 1:
        print(
            "Recordando la advertencia del pequeño granjero, tomas tus armas y te avalanzas sobre el esqueleto"
        )
        print(combate(jugador, Esqueleto()))


def entrada2():
    print("Etrada")
    print("")
    print(
        "El pasadizo oriental esta lleno de telarañas y parece q no se ha usado desde mucho tiempo"
    )
    print("")
    print(
        "el pasadizo occidental huele a paja y moho, pero esta limpio de telarañas"
    )
    crea_enemigo()
    direc = input("(pasadizo oriental/pasadizo occidental) :")
    if direc == "pasadizo oriental":
        pasillo_oriental()
    elif direc == "pasadizo occidental":
        pasillo_occidental()


def trampa():
    print(
        "Viendo que no hay monstruos en la habitación, avanzas hacia las escaleras mientras vas recogiendo monedas"
    )
    print(
        "por el camino. A media habitación tu pie se engancha en un alambre oculto y de repente un chorro de llamas"
    )
    print("sa disparado de la boca del demonio, ¡directamente hacia ti!")
    fuego = random.randint(10, 20)
    jugador.puntos_golpe -= fuego
    print("el fuego te causa un daño de", fuego)
    print("tus puntpos de vida son", jugador.puntos_golpe)
    if (jugador.puntos_golpe >= 0):
        print(monedas())

    else:
        print(
            "Ruedas para apagar las llamas pero finalmente terminas envuelto en ellas"
        )
        print("Estas muerto")
        sys.exit()


def monedas():
    print("un enemigo se mueve en tu direccion")
    print(combate(jugador, Rata()))
    print(
        "El fuego te quemo un poco pero conseguiste sobrevivir y cuentas tu botin"
    )
    print("la estatua continua como si nada y las escaleras abajo ")
    print("¿Estas preparado para explorar el nivel inferior?")
    print("")
    direc = input("(regresar/bajar escaleras ):")
    monedas = random.randint(2, 9)
    jugador.dinero += monedas

    if direc == "regresar":
        entrada2()

    elif direc == "bajar escaleras":
        escalera()


def escalera():
    crea_enemigo()
    print(
        "las antiguas escalera de piedra etan resbaladizas por la humedad. Cuando llegas al fondo descubres que"
    )
    print(
        "terminan en una gran caverna natural llena de estalactitas y estalagamitas."
    )
    print(
        "Puedes ver charcos superficiales de agua en el suelo, y una gran grieta en la pared del fondo que parce un pasadizo."
    )
    print(
        "A medida que cruzas la habitación algo no te cuadra. Te detienes para mirar a tu alrededor"
    )
    resultado = random.randint(1, 10)
    if resultado >= 4:
        print(
            "De repente te das cuenta que te estaba preocupando y te detienes. justo donde ivas a poner el pie hay una mancha de moho"
        )
        print(
            "de color amarillo pegada a la piedra. Ya has oido historias sobre estas cosas: moho amarillo que crece en cuevas parece inofensivo"
        )
        print(
            "hasta que lo molestas, momento en el que libera millones de esporas venenozas que ahogan a exploradores imprudentes"
        )
        print(
            "Retiras el pie y das vuelta con cuidado para rodear el moho. Habiendo evitado el desastre, te dirigis hacia la grieta del fondo"
        )
        print(
            "y descubres que realmente es un pasadizo. Mas adelantepuedes ver una luz parpadeante, puedes oir el sonido de huesos entrechocando"
        )
        print("")
        lucha = input("(entrar/regresar) :")
        if lucha == "entrar":
            sala_jefe()

        elif lucha == "regresa":
            entrada2()

    if resultado <= 3:
        print(
            "Aunque no puedes quitarte de ensima la sensación de que algo anda mal, te armas de valor y sigues adelante. No obstante,"
        )
        print(
            "cuando con tinuas con tu camino, tu bota pisa un trozo informe de moho que crece en la piedra."
        )
        print(
            "De repente se produce se produce un gran sonido sibilante, y el aire atu alrededor se llena de esporas amarillas"
        )
        print(
            "que aparecen en todas partes, te llenan la boca y la nariz. Las esporas te hacen toser y te ahogan, haciendo que"
        )
        print("te lloren los ojos, y sientas debilidad en los brazos.")
        print("pizaste un hongo toxico.")
        cura = random.randint(1, 3)
        jugador.puntos_golpe -= cura
        print("vida: ", jugador.puntos_golpe)
        sala_jefe()
        print("")
        if jugador.vida >= 0:
            print(
                "Las esporas se asientan y puedes ver de nuevo atravez de tus lagrimas teñidas de amarillo,"
            )
            print(
                "llegas a la grieta del fondo del fondo de la habitación. Alli"
            )
            print(
                "descubres que realmente es un pasadizo. Mas adelantepuedes ver una luz parpadeante, puedes oir el sonido de huesos entrechocando"
            )
            sala_jefe()
        if jugador.vida <= 0:
            print("GAME OVER")


def pasillo_oriental():
    print("")
    print(
        "Esta lleno de telarañas parece q no se ha utilizado en mucho tiempo.")
    print(
        "Usas la antorcha para quemar las telarañas y te adentras cuidadosamente por el pasadizo. "
    )
    print(
        "Tras unos metros el pasadizo gira al sur y avazas otros metros antes de abrirce una gran sala"
    )
    print(
        "Esta gran sala está vacia exepto por las telarañas que cuelgan del techo. Al otro lado, encima de una puerta"
    )
    print(
        "abierta puedes ver la grotesca escultura de un demonio. En el suelo brillan, aqui y alla, algunas monedas de oro"
    )
    print("")
    print(
        "y atravez de la puerta puede ver puedes ver un tramo de escaleras que se adentra mas en lo profundo"
    )
    direc = input("(recoger monedas/bajar escaleras/ regresar) :")
    print("")
    if direc == "recoger monedas":
        print("")
        trampa()
    elif direc == "bajar escaleras":
        print("")
        escalera()
    elif direc == "regresar":
        entrada2()


def pasillo_occidental():
    crea_enemigo()
    print("")
    print("Huele a paja y moho")
    print(
        "El olor a moho se hace más fuerte a medida que te internas en el pasillo. Tras unos metros"
    )
    print(
        "termina en una puerta sencilla de madera, que esta semi abierta a la siguiente habitación"
    )
    print("")
    opcion = input("(entrar/regresar) :")
    if opcion == "entrar":
        if jugador.evento == 0:
            habitacion1()

        elif jugador.evento == 1:
            habitacion1_1()

    if opcion == "regresar":
        entrada2()


def habitacion1_1():
    crea_enemigo()
    print(
        "La habitacion ahora se encuento vacia, decides regresar a la entrada")
    entrada2()


def habitacion1():
    print(
        "Dentro de la habitació hay una gran caja hecha de barrotes de hierro, y una capa de paja mohosa en el fondo"
    )
    print(
        "Parece hambriento y está cubierto de mallugadoras. Al otro lado de la habitación hay una trampa colgando de un gancho"
    )
    print(
        "a unos pocos pies del suelo, lo suficientemente alto como para que llegue un goblin. Parece que el niño esta dormido."
    )
    print("")
    desicion = input("(tomar llave/despertar niño/salir) :")
    if desicion == "tomar llave":
        print("depronto uno goblin que patrullan la zona te descubre")
        print(combate(jugador, Goblin()))
        despertar()

        print(
            "Descuelgas la llave parece que en caja en la cerradura de la jaula"
        )
        desicion_nino = input("(despertar niño/ignorar) :")
        print("")
        espada()

    if desicion == "despertar niño":
        print("")
        despertar()

    if desicion == "ignorar":
        print(
            "Estas muy asustado de caer en una trampa y regresas a la entrada")
        print("")
        entrada2()


def espada():
    print(
        "¡Gracias! gime el niño cuando le abres la puerta de la jaula. Llevo aqui encerrado muchos dias,"
    )
    print(
        "ten cuidado hay algo mas terrible que un goblin mas en lo profundo.")
    print(
        "Toma esto logre robarla de un goblin pero no tube el valor de uzarla el niño te da una espada corta(fuerza +2)"
    )
    jugador.fuerza += 2
    print("luego sale corriendo en direccion a la salida")
    print("Regresas a la entrada")
    jugador.evento = 1
    print("vida: ", jugador.puntos_golpe, "fuerza: ", jugador.fuerza)
    habitacion1_1()


def despertar():
    print(
        "Despiertas el niño y sus ojos se abren lentamente ¡Gracias a los dioses! dice con voz ronca a travéz de sus labios, el niño te advierte que pueden haber goblin patrullando la zona tomas la llave temeroso de caer en una trampa"
    )
    print("agrietados y ensangrentados.")
    print("Tomas la llave cautelso de que todo no sea una trampa")
    disicion_nino = input("(introducir llave/ignorar) :")
    print("")
    if disicion_nino == "introducir llave":
        print(
            "¡Gracias! gime el niño cuando le abres la puerta de la jaula. Llevo aqui encerrado muchos dias,"
        )
        print(
            "ten cuidado hay algo mas terrible que un goblin mas en lo profundo."
        )
        print(
            "Toma esto logre robarla de un goblin pero no tube el valor de uzarla el niño te da una espada corta(fuerza +2)"
        )
        print("luego sale corriendo en direccion a la salida")
        jugador.fuerza += 2
        print("vida: ", jugador.puntos_golpe, "fuerza: ", jugador.fuerza)
        jugador.item = 1
        habitacion1_1()

    else:
        ("Ignoras las suplicas del niño y regresas a la entrada")
        entrada2()


def entrada():

    print(
        "Te encuentras en un pasadizo oscuro y polvoriento que se adentra en la tierra. A medida\
  que caminas, la luz de la entrada se desvanece rapidamente hasta ser sólo un brillo tenue, así que\
  que te ves obligado a usar una antorcha para iluminar tu camino. A su luz parpadeante puedes ver\
  que el pasadizo se abre en seguida a una habitación. Oyes un gruñido grave, y sacas tu espada de la funda"
    )
    print("")
    print(
        "De repente tus ojos detectan movimiento, un montón de harapos en una esquina se levantan\
  y resulta ser un infame goblinde verrugosa piel verde, y cabezacon forma de sandia. Sus sucias\
  ropas estan cubiertas de manchas de sangre, y en una mano aún sotiene la pata asadas de una oveja\
  robada. En su otra mano lleva una espada corta de aspecto perverso.")
    print("")
    print("¡Te lanza un gruñido y carga!")
    print("")

    encuentro = input("¿sacar arma/hablar? :")
    if encuentro == "sacar arma":
        print(
            "Sabes que el goblin es una criatura desagradable y maligna que deves matar antes de continuar"
        )
        print(combate(jugador, Goblin()))
        print(
            "Con una envestida final, supera la guardia del goblin y hundes tu espada en su pecho."
        )
        print(
            "El goblin gruñe de dolor y frustarcion por ultima vez, y despues sus inchados ojos se cierran"
        )
        print(
            "y cae al suelo muerto. Echas un vistaso a la mugrienta bolsa que lleva en el cinturon"
        )
        print(
            "encuentras 7 piezas de oro y un pequeño vial lleno de liquido rojo. En el tapon se lee CURAR."
        )

        print("")
        jugador.dinero += 7
        print(camino())

    else:
        print(
            "El goblin se abalanza sobre ti, corres embusca de la salida pero te tropiesas con las piedras el goblin salta a tu espalda y te apuñala"
        )
        print("")
        print("Estas muerto")
        print("GAME OVER")
        print("")
        sys.exit()


def usuario():
    usuario = 0
    while usuario <= 0:
        print("Hola jugador forja tu destino, ¿quien deseas ser?")
        ready = input("Airón,Clair,Varg,Pat,Tyr :")
        print(linea_punteada)
        if ready == "airon":
            jugador = Player("Airón", "Humanoide", "Guerrero", 8, 3, 3, 6, 0,
                             0, 2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             {})
            usuario = 0 + 1
            print(atributos())

        elif ready == "clair":
            jugador = Player("Clair", "Humano", "Explorador", 6, 2, 1, 6, 0, 1,
                             8, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             {})
            usuario = 0 + 1
            print(atributos())

        elif ready == "varg":
            jugador = Player("Varg", "Semi orco", "Asesino", 6, 2, 2, 8, 2, 2,
                             6, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             {})
            usuario = 0 + 1
            print(atributos())

        elif ready == "pat":
            jugador = Player("Pat", "Elfo", "Mago", 6, 0, 0, 6, 2, 2, 8, 2, 2,
                             0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {})
            usuario = 0 + 1
            print(atributos())

        elif ready == "tyr":
            jugador = Player("Tyr", "Caido", "Explorador", 6, 1, 1, 8, 2, 2, 6,
                             1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {})
            usuario = 0 + 1
            print(atributos())

        print("opcion no soportada")
        print("")


def combate(luchador, contrincante):
    print("Un enemigo", contrincante.nombre,
          " a la vista sus puntos de vida son", contrincante.puntos_golpe)
    print(linea_punteada)
    jd_ini = random.randint(1, 20) + luchador.iniciativa
    je_ini = random.randint(1, 20) + contrincante.iniciativa
    if (jd_ini >= je_ini):
        print("Atacas primero! tu velocidad fue de ", jd_ini)
        print(textwrap.fill(linea_punteada))
        combate = input(
            "tienes la oportunidad de hacer un ataque: a) ataque sigiloso/ b) ojo de aguila/ c) cargar/ d) lanzar hechizo  :"
        )
        print(linea_punteada)
        if combate == "a" and jugador.clase == "Asesino":
            print("te esacabuyes en las sombras")
            jd_sig = random.randint(1,
                                    20) + luchador.dextresa + luchador.agilidad
            je_alert = random.randint(
                1, 20) + contrincante.mente + contrincante.intelecto
            if (jd_sig >= je_alert):
                contrincante.puntos_golpe -= (
                    luchador.dextresa + luchador.movilida)
                print("con un ataque repentino, el", contrincante.nombre,
                      "le quedan", contrincante.puntos_golpe)
                print("Tiene", contrincante.puntos_golpe, "puntos de vida")
                print(linea_punteada)
            else:
                print(contrincante.nombre, "te descubre y te ataca")
                print("El daño fue de ", contrincante.fuerza)
                luchador.puntos_golpe -= contrincante.fuerza
                print("Te quedan", luchador.puntos_golpe, "puntos de vida")
                print(linea_punteada)

        elif combate == "b" and jugador.clase == "Explorador":
            jd_atkd = random.randint(
                1,
                20) + luchador.dextresa + luchador.agilidad + luchador.fuerza
            je_defd = random.randint(
                1, 20
            ) + contrincante.mente + contrincante.intelecto + contrincante.defensa
            if jd_atkd > je_defd:
                daño_flecha = (
                    luchador.dextresa + luchador.movilida + luchador.fuerza)
                print("Sacas una flecha causando un daño de", daño_flecha)
                print(contrincante.nombre, "tiene", contrincante.puntos_golpe,
                      "puntos de vida")
                print(linea_punteada)
            else:
                daño_ene = (contrincante.dextresa + luchador.agilidad +
                            luchador.fuerza)
                print(contrincante.nombre, "esquiva tu flecha", je_defd,
                      "corre a tu encuentro y te causa un daño de", daño_ene)
                print(linea_punteada)

        elif combate == "c" and jugador.clase == "Guerrero":
            carga = random.randint(1, 20) + (
                luchador.constitucion + luchador.movilida + luchador.fuerza)
            esquivar = random.randint(
                1, 20) + (contrincante.agilidad + contrincante.movilida)
            if carga > esquivar:
                contrincante.puntos_golpe - (luchador.constitucion + luchador.
                                             movilida + luchador.fuerza)
                print("Tu carga de", carga, "sorprende a", contrincante.nombre,
                      "causando daño", contrincante.puntos_golpe)
                print(linea_punteada)

            else:
                luchador.puntos_golpe -= (
                    contrincante.agilidad + contrincante.movilida)
                print(
                    contrincante.nombre,
                    "se percata de tu ataque esquivandolo y causandote daño tu vida es",
                    luchador.puntos_golpe)
                print(linea_punteada)

        elif combate == "d" and jugador.clase == "Mago":
            hechizo = random.randint(
                1, 20) + (luchador.hechizoDirigido + luchador.aura)
            fallar = random.randint(1, 20) + (luchador.aura + luchador.mente)
            if hechizo > fallar:
                contrincante.puntos_golpe - (
                    luchador.hechizoDirigido + luchador.hechizeria)
                print("Tu echizo logra golpear a", contrincante.nombre,
                      "le quedan", contrincante.puntos_golpe)
                print(linea_punteada)
            else:
                luchador.puntos_golpe - (
                    contrincante.mente + contrincante.aura)
                print("Tu echizo falla y pone alerta a", contrincante.nombre,
                      "y te ataca")
                print(linea_punteada)

    else:
        print(contrincante.nombre, "ataca primero! su velocidad fue de ",
              je_ini)
        je_atk = random.randint(1, 20) + contrincante.fuerza
        jd_def = random.randint(1, 20) + luchador.defensa
        if (je_atk >= jd_def):
            print(contrincante.nombre,
                  "lanza su ataque! su fuerza de ataque fue de ", je_atk)
            je_daño = random.randint(1, 20) + contrincante.atkcuerpoAcuerpo
            jd_blk = random.randint(1, 20) + luchador.defensa
            if (je_daño >= jd_blk):
                jugador.puntos_golpe -= (luchador.movilida + luchador.dextresa)
                print("Resibes el daño de su ataque tus puntos de vida son",
                      jugador.puntos_golpe)
                print(linea_punteada)

            else:
                print("Bloqueas el ataque! tu defensa fue de ", jd_blk)
                print(linea_punteada)
        else:
            print("Logras esquivar el ataque! tu velocidad fue de ", jd_def)
            print(linea_punteada)

    while luchador.puntos_golpe > 0:
        print(linea_punteada)
        combate = input(
            "a) atacar/ b) ataque a distancia/ c) lanzar magia d) item/ e) ataque veloz/ f) Golpe contundente/ g) escapar :"
        )
        print(linea_punteada)
        print(contrincante.nombre, "tiene", contrincante.puntos_golpe,
              "puntos de vida")

        if combate == "g":
            jd_esc = random.randint(1,
                                    20) + luchador.movilida + luchador.agilidad
            je_vel = random.randint(
                1, 20
            ) + contrincante.movilida + contrincante.agilidad + contrincante.dextresa
            if jd_esc > je_vel:
                print("Logras escapar a gran velocidad")
                print(linea_punteada)
                return

            else:
                print("No logras escapar")
                je_desc = (contrincante.movilida + contrincante.agilidad)
                print(
                    contrincante.nombre,
                    "te ataca a gran velocidad cuando escapas haciendote un daño de",
                    je_desc)
                print(linea_punteada)

        elif combate == "f" and luchador.clase == "Guerrero":
            jd_atkf = random.randint(1, 20) + (
                luchador.fuerza + luchador.constitucion + luchador.cuerpo)
            je_esqf = random.randint(1, 20) + contrincante.defensa
            if jd_atkf >= je_esqf:
                print("Tu ataque brutal", je_esqf,
                      "rompe la defenza de tu enemigo", je_esqf)
                contrincante.puntos_golpe -= (
                    luchador.fuerza + luchador.constitucion + luchador.cuerpo)
                print("Le quedan", contrincante.puntos_golpe)
                print(linea_punteada)

            else:
                print(contrincante.nombre, "se resite a tu ataque de", jd_atkf,
                      "con una defenza de", je_esqf)
                luchador.puntos_golpe - (
                    contrincante.fuerza + contrincante.constitucion)
                print("Te quedan", luchador.puntos_golpe, "puntos de vida")
                print(linea_punteada)

        elif combate == ("d"):
            print("no tienes items")

        elif combate == "e" and jugador.clase == "Asesino":
            jd_atkv = random.randint(
                1, 20) + luchador.dextresa + luchador.agilidad
            je_esqv = random.randint(
                1, 20) + contrincante.dextresa + luchador.agilidad
            if jd_atkv > je_esqv:
                print("A gran velocidad lanzas un ataque de", jd_atkv)
                contrincante.puntos_golpe - (
                    luchador.fuerza + luchador.dextresa + luchador.agilidad)
                print("A tu enemigo le quedan", contrincante.puntos_golpe)
                print(linea_punteada)
            else:
                print("El enemigo logra esquivar tu ataque", je_esqv,
                      "tu velocidad fue de", jd_atkv)
                print(linea_punteada)

        elif combate == "c" and jugador.clase == "Mago":
            print("Lanzas un echizo de nivel 1")
            jd_hec = random.randint(1, 20)
            je_defh = random.randint(
                1, 20
            ) + contrincante.intelecto + contrincante.aura + contrincante.mente
            if jd_hec > je_defh:
                daño_hechizo = contrincante.puntos_golpe - jd_hec
                contrincante.puntos_golpe -= jd_hec
                print("Tu echizo causa un daño de ", daño_hechizo)
                print("El enemigo tiene", contrincante.puntos_golpe, "de vida")
                print(linea_punteada)
            else:
                luchador.puntos_golpe -= (
                    contrincante.mente + contrincante.aura)
                print(
                    contrincante.nombre,
                    "resiste a tu echizo causandote daño ahora tus puntos de vida son",
                    luchador.puntos_golpe)
                print(linea_punteada)

        elif combate == "b" and jugador.clase == "Explorador":
            jd_atkd = random.randint(1, 20) + luchador.atkAdistancia
            je_evad = random.randint(
                1, 20) + contrincante.dextresa + contrincante.agilidad
            if (jd_atkd >= je_evad):
                print("te alejas y sacas tu arco y aputas con una fuerza de ",
                      jd_atkd)
                contrincante.puntos_golpe -= (
                    luchador.atkAdistancia + luchador.fuerza)
                print("le causas daño ahora sus puntos de vida son",
                      contrincante.puntos_golpe)
                print(linea_punteada)

            else:
                print("el enemigo", contrincante.nombre,
                      "esquiva el ataque con una velocidad de", je_evad)
                print("se acerca y te ataca a gran velocidad")
                je_atkvel = (contrincante.agilidad + contrincante.movilida)
                jugador.puntos_golpe -= (
                    contrincante.movilida + contrincante.agilidad)
                print("el enemigo ataca a una velocidad de", je_atkvel,
                      "ahora se encuentra muy serca de ti")
                print("te quedan", jugador.puntos_golpe, "de vida")
                print(linea_punteada)

        elif combate == ("a"):
            jd_atk = random.randint(
                1,
                20) + luchador.fuerza + luchador.constitucion + luchador.cuerpo
            je_def = random.randint(1, 20) + contrincante.defensa
            if (jd_atk >= je_def):
                print("Lanzas tu ataque! tu fuerza de ataque fue de ", jd_atk)
                jd_daño = random.randint(1, 20) + luchador.atkcuerpoAcuerpo
                je_blk = random.randint(1, 20)
                if (jd_daño >= je_blk):
                    contrincante.puntos_golpe -= luchador.constitucion
                    print("Le haces daño y le quedan ",
                          contrincante.puntos_golpe, " puntos de vida")
                    print(linea_punteada)
                else:
                    print("tu ataque fue de", jd_daño,
                          "pero el enemigo bloque tu ataque", je_blk,
                          "y contraataca")
                    luchador.puntos_golpe -= (
                        contrincante.fuerza + contrincante.fuerza)
                    print("te quedan", luchador.puntos_golpe, "puntos de vida")
                    print(linea_punteada)
            else:
                print("Tu ataque fue de", jd_atk,
                      "el enemigo bloquea tu ataque", je_def)
                luchador.puntos_golpe -= contrincante.fuerza
                print("Arremete con un ataque de", contrincante.fuerza,
                      "te quedan", luchador.puntos_golpe)
                print(linea_punteada)

        if contrincante.puntos_golpe <= 0:
            contrincante.vivo = False
            print("Ganaste!")
            luchador.xp += random.randint(20, 30)
            luchador.dinero += random.randint(2, 8)
            print("Te quedan ", luchador.puntos_golpe, "puntos de vida")
            print("Tienes ", luchador.dinero, " monedas de oro")
            print("Tienes", luchador.xp, "de experiencia")
            descanso = random.randint(1, 4)

            if descanso == 1:
                luchador.puntos_golpe += 1
                print(
                    "Tras unos momentos de descanzo recuperas 1 puntos de vida ahora son",
                    luchador.puntos_golpe)
                print(linea_punteada)

            elif descanso == 4:
                print(
                    "continuas tu camino con la intencion de abandonar pronto este lugar"
                )

            elif descanso == 2:
                luchador.puntos_golpe += 3
                print(
                    "Tras unos momentos de descanzo recuperas 3 puntos de vida ahora son",
                    luchador.puntos_golpe)
                print(linea_punteada)

            elif descanso == 3:
                luchador.fuerza += 2
                print(
                    "Tras unos momentos de descanzo encuentras un amuleto que aumenta tu fuerza en 2 y ahora tu fuerza es de",
                    luchador.fuerza)
                print(linea_punteada)
            comprobar_lvl(jugador)

            if contrincante.vivo == False:
                break

        elif jugador.puntos_golpe <= 0:
            print("el enemigo", contrincante.nombre, "te a matado")
            luchador.vivo = False
            if contrincante.vivo == False:
                print("Tu enemigo", contrincante.nombre,
                      "se regosija por su victoria")
                sys.exit()

    else:
        print("accion no soportada")
        print(linea_punteada)


def inicio():
    print("LA CRIPTA DEL REY ESQUELETO")
    print("---------------------------")
    print("                           ")
    print(
        "Eres un valiente", jugador.clase, "procedente del pueblo \
  de Punta Arena, situado en la tierra de Varisia, en la costa \
  del gran mar Humeante. la vida en el pueblo es sencilla pero también dura, ya que las\
  tierras salvajes que lo rodean están infestadas de goblin y otros monstruos."
    )
    print("")
    print("Últimamente los monstruos se han vuelto más atrevidos, llevándose \
  niños y ganado del las granjas más alejadas. Los habitantes, aterrados, han recurrido a\
  ti para que les protejas. La alcaldesa, una amable mujer llamada Kendra Deverin, \
  te ha prometido una recompensa de 100 piezas de oro si limpias un dungeon cercano \
  donde se dice que viven tales criaturas. Es un trabajo peligroso, \
  pero te notas listo para el desafio.")
    print("")
    print(
        "Preparas tu equpo, una resitente armadura de cota de mallas, y una antigua espada\
  larga de tu padre, y te diriges hacia el bosque, siguiendo el tosco mapa que te dio \
  la alcaldesa. Tras varias horas caminando llegas a una desolada ladera. Justo por \
  ensima de ti se abre la entrada oscura de un tunel.")
    print("")

    print(" ¡Éste debe ser el dungeon!")
    print("")
    print("¿Quieres armarte de valor y entrar en el tunel, ", jugador.nombre,
          "?")
    print("")
    respuesta = input("(si/no) :")

    if respuesta == "si":
        print("")
        print(entrada())

    else:
        print("COBARDE!")



