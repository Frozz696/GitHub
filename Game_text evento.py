import random
import sys
import os

personaje={"eventos":{"espada" : True}}

Equipo = {"Armadura":"Cota de mallas","Arma":"Antigua espada larga"}

def recompensa(personaje):
    personaje == random.randint(1,3)
    print ("Encuentras una pócima curativa")
    pocion_cura()
    
    personaje == random.randint(1,3)
    print ("Encuentras una pócima de un aspegto repugnate")
    pocion_stats()
    print ("")
    
def comprobar_lvl(personaje):
    if personaje["xpSiguientelvl"] >= personaje["xp"]:
        if personaje["nivel"] + 1:
           personaje["xpSiguientelvl"] = 0
           personaje["vida"] += 2
           personaje["fuerza"] += 1
           print("vida: ",personaje["vida"],"fuerza: ",personaje["fuerza"])
           print ("Tus fuerzas aumentan!")
           print("")
        

def printestado():
    print("vida: ",personaje["vida"],"dinero: ",personaje["dinero"])

def pocion_cura():
    cura = random.randint(0,1)
    personaje["vida"] += cura
    print("vida: ",personaje["vida"])
    print ("")

def pocion_stats():
    stats = random.randint(0,1)
    personaje["fuerza"] += stats
    print("fuerza: ",personaje["fuerza"])
    print("")

def entrada2():
  print ("Etrada")
  print ("")
  print ("El pasadizo oriental esta lleno de telarañas y parece q no se ha usado desde mucho tiempo")
  print ("")
  print ("el pasadizo occidental huele a paja y moho, pero esta limpio de telarañas")
  creaLootbox()
  direc = input ("(pasadizo oriental/pasadizo occidental) :")
  if direc == "pasadizo oriental":
    pasillo_oriental()
  elif direc == "pasadizo occidental":
    pasillo_occidental()


def trampa():
  print ("Viendo que no hay monstruos en la habitación, avanzas hacia las escaleras mientras vas recogiendo monedas")
  print ("por el camino. A media habitación tu pie se engancha en un alambre oculto y de repente un chorro de llamas")
  print ("sa disparado de la boca del demonio, ¡directamente hacia ti!")
  daño_trampa = random.randint(2,4)
  creaLootbox()
  personaje["vida"] -= daño_trampa
  printestado()
  if personaje["vida"] <= 0: 
    print("Ruedas para apagar las llamas pero finalmente terminas envuelto en ellas")
    print("Estas muerto")
    printestado()
    sys.exit()
  else:
      print("El fuego te quemo un poco pero conseguiste sobrevivir y cuentas tu botin")
      print("la estatua continua como si nada y las escaleras abajo ")
      print("¿Estas preparado para explorar el nivel inferior?")
      print ("")
      direc = input ("(regresar/bajar escaleras ):")
      monedas = random.randint (2,9)
      personaje["dinero"] += monedas
      printestado()
      if direc == "regresar":
       entrada2()
       
      elif direc == "bajar escaleras":
       entrada2()

    
    
def escalera():
  print("las antiguas escalera de piedra etan resbaladizas por la humedad. Cuando llegas al fondo descubres que")
  print ("terminan en una gran caverna natural llena de estalactitas y estalagamitas.")
  print ("Puedes ver charcos superficiales de agua en el suelo, y una gran grieta en la pared del fondo que parce un pasadizo.")
  print ("A medida que cruzas la habitación algo no te cuadra. Te detienes para mirar a tu alrededor")
  resultado = random.randint(1,10)
  if resultado >= 5:
      print ("De repente te das cuenta que te estaba preocupando y te detienes. justo donde ivas a poner el pie hay una mancha de moho")
      print ("de color amarillo pegada a la piedra. Ya has oido historias sobre estas cosas: moho amarillo que crece en cuevas parece inofensivo")
      print ("hasta que lo molestas, momento en el que libera millones de esporas venenozas que ahogan a exploradores imprudentes")
      print ("Retiras el pie y das vuelta con cuidado para rodear el moho. Habiendo evitado el desastre, te dirigis hacia la grieta del fondo")
      print ("y descubres que realmente es un pasadizo. Mas adelantepuedes ver una luz parpadeante, puedes oir el sonido de huesos entrechocando")
      print ("")
      lucha = input ("(entrar/regresar) :")
      if lucha == "entrar":
          entrada2()
      
      elif lucha == "regresa":
          entrada2()
  
  if resultado <= 4:
      print ("Aunque no puedes quitarte de ensima la sensación de que algo anda mal, te armas de valor y sigues adelante. No obstante,")
      print ("cuando con tinuas con tu camino, tu bota pisa un trozo informe de moho que crece en la piedra.")
      print ("De repente se produce se produce un gran sonido sibilante, y el aire atu alrededor se llena de esporas amarillas")
      print ("que aparecen en todas partes, te llenan la boca y la nariz. Las esporas te hacen toser y te ahogan, haciendo que")
      print ("te lloren los ojos, y sientas debilidad en los brazos.")
      print ("pizaste un hongo toxico.")
      cura = random.randint(1,3)
      personaje["vida"] -= cura
      print("vida: ",personaje["vida"])
      print ("")
      if personaje["vida"] >= 0:
          print ("Las esporas se asientan y puedes ver de nuevo atravez de tus lagrimas teñidas de amarillo,")
          print ("llegas a la grieta del fondo del fondo de la habitación. Alli")
          print ("descubres que realmente es un pasadizo. Mas adelantepuedes ver una luz parpadeante, puedes oir el sonido de huesos entrechocando")
      if personaje["vida"] <= 0:
            print("GAME OVER")
      

def pasillo_oriental():
  print ("")
  print ("Esta lleno de telarañas parece q no se ha utilizado en mucho tiempo.")
  print("Usas la antorcha para quemar las telarañas y te adentras cuidadosamente por el pasadizo. ")
  print ("Tras unos metros el pasadizo gira al sur y avazas otros metros antes de abrirce una gran sala")
  print ("Esta gran sala está vacia exepto por las telarañas que cuelgan del techo. Al otro lado, encima de una puerta")
  print ("abierta puedes ver la grotesca escultura de un demonio. En el suelo brillan, aqui y alla, algunas monedas de oro")
  print ("")
  print ("y atravez de la puerta puede ver puedes ver un tramo de escaleras que se adentra mas en lo profundo")
  direc = input ("(recoger monedas/bajar escaleras/ regresar) :" )
  print("")
  if direc == "recoger monedas":
    print ("")
    trampa()
  elif direc == "bajar escaleras":
    print("")
    escalera()
  elif direc == "regresar":
    entrada2()  
 

def pasillo_occidental():
  print("")
  print ("Huele a paja y moho")
  print ("El olor a moho se hace más fuerte a medida que te internas en el pasillo. Tras unos metros")
  print("termina en una puerta sencilla de madera, que esta semi abierta a la siguiente habitación")
  print ("")
  opcion = input ("(entrar/regresar) :")
  if opcion == "entrar":
      if personaje["item"] == 0:
          habitacion1()
          
      elif personaje["item"] == 1:
          habitacion1_1()
          
  if opcion == "regresar":
    entrada2()
    
def habitacion1_1():
        print ("La habitacion ahora se encuento vacia, decides regresar a la entrada")
        entrada2()
    
def habitacion1():
    print ("Dentro de la habitació hay una gran caja hecha de barrotes de hierro, y una capa de paja mohosa en el fondo")
    print ("Parece hambriento y está cubierto de mallugadoras. Al otro lado de la habitación hay una trampa colgando de un gancho")
    print ("a unos pocos pies del suelo, lo suficientemente alto como para que llegue un goblin. Parece que el niño esta dormido.")
    print ("")
    desicion = input ("(tomar llave/despertar niño/salir) :")
    if desicion == "tomar llave":
            despertar()
            
            print ("Descuelgas la llave parece que en caja en la cerradura de la jaula")
            desicion_nino = input ("(despertar niño/ignorar) :")
            print("")
            espada()
            
    if desicion == "despertar niño":
            print ("")
            despertar()
        
    if desicion == "ignorar":
            print ("Estas muy asustado de caer en una trampa y regresas a la entrada")
            print("")
            entrada2()

def espada():
        print ("¡Gracias! gime el niño cuando le abres la puerta de la jaula. Llevo aqui encerrado muchos dias,")
        print ("ten cuidado hay algo mas terrible que un goblin mas en lo profundo.")
        print ("Toma esto logre robarla de un goblin pero no tube el valor de uzarla el niño te da una espada corta(fuerza +2)")
        print ("luego sale corriendo en direccion a la salida")
        print ("Regresas a la entrada")
        personaje["item"] = 1
        print("vida: ",personaje["vida"],"fuerza: ",personaje["fuerza"])
        habitacion1_1()

def despertar():
        print ("Despiertas el niño y sus ojo se abren lentamente ¡Gracias a los dioses! dice con voz ronca a travéz de sus labios,tomas la llave temeroso de caer en una trampa")
        print ("agrietados y ensangrentados.")
        print ("Tomas la llave cautelso de que todo no sea una trampa")
        disicion_nino = input ("(introducir llave/ignorar) :")
        print("")
        if disicion_nino == "introducir llave":
            print ("¡Gracias! gime el niño cuando le abres la puerta de la jaula. Llevo aqui encerrado muchos dias,")
            print ("ten cuidado hay algo mas terrible que un goblin mas en lo profundo.")
            print ("Toma esto logre robarla de un goblin pero no tube el valor de uzarla el niño te da una espada corta(fuerza +2)")
            print ("luego sale corriendo en direccion a la salida")
            personaje["fuerza"] += 2
            print("vida: ",personaje["vida"],"fuerza: ",personaje["fuerza"]) 
            personaje["item"] = 1
            habitacion1_1()
    
        else:
            ("Ignoras las suplicas del niño y regresas a la entrada")
            entrada2()
 
def goblin (vida,fuerza):
  print ("¡tiene",vida,"puntos de vida!")
  while personaje["vida"] > 0:
    accion = input("¿atacar,correr? :")
    print("Al goblin le quedan",vida,"puntos de vida")
    printestado()
    personaje["vida"] -= fuerza
    if accion == "atacar":
      vida = (vida - personaje["fuerza"])
      print ("")
      print ("!El goblin ataca!")
      if vida <= 0:
        print ("Con una envestida final, supera la guardia del goblin y hundes tu espada en su pecho.")
        print ("El goblin gruñe de dolor y frustarcion por ultima vez, y despues sus inchados ojos se cierran")
        print (" y cae al suelo muerto. Echas un vistaso a la mugrienta bolsa que lleva en el cinturon")
        print (" y encuentras 7 piezas de oro y un pequeño vial lleno de liquido rojo. En el tapon se lee CURAR.")
        print ("")
        print ("¡Debe ser una poción de curacion!")
        print ("")
        print ("Mirando a tu alrededor puedes ver que el resto de la sala esta vacio, pero hay dos pasadizos que salen")
        print ("de la habitacion y se adentran más profundamente en el dungeon")
        personaje["dinero"] += 7
        pocion_cura()
        xp = random.randint(8,12)
        personaje["xpSiguientelvl"] += xp
        print("XP: ",personaje["xpSiguientelvl"])
        comprobar_lvl(personaje)
        direc = input ("(pasadizos oriental/pasadizo occidental) :")
        if direc == "pasadizo oriental":
          pasillo_oriental()
        elif direc == "pasadizo occidental":
          pasillo_occidental()
      else:
        accion = input("¿atacar,correr? :")
        print("Al goblin le quedan",(vida),"puntos de vida")
        printestado()
        print("")
        personaje["vida"] -= fuerza
        if accion == "atacar":
          vida = (vida - personaje["fuerza"])
          print ("")
          print ("!El goblin ataca!")
        if personaje["vida"] <= 0:
          print ("El goblin te apuñala, mientras das tu ultimo aliento observas el goblin saquear tus pertenencias")
          print ("Estas muerto")
          printestado()
          sys.exit()
    else:
      print("El goblin ataca!!")
      print ("Corres despavorido")
      entrada2()

def creaLootbox ():
  loot = random.randint(1,12)
  if loot % 3 == 0:
    loot_vida = random.randint(9,16)
    loot_fuerza = random.randint(2,4)
    lootbox(loot_vida,loot_fuerza)

def lootbox (vida,fuerza):
  print("¡Una Lootbox salvaje apareció!")
  print("¡Tiene",vida,"puntos de vida!")
  while personaje["vida"] > 0:
    print("")
    accion = input("¿atacar/escapar? :")
    print ("")
    if accion == "atacar":
      vida = vida - personaje["fuerza"]
      if vida <= 0:
        print("Ganaste!!!!")
        print("Tu premio es 2 monedas")
        recompensa(personaje)
        personaje["dinero"] += 2
        xp = random.randint(8,12)
        personaje["xpSiguientelvl"] += xp
        comprobar_lvl(personaje)
        print("XP: ",personaje["xpSiguientelvl"])
        entrada2()
      else:
        print("A la Lootboox le quedan",vida,"puntos de vida")
        print("La Lootbox ataca!!!!")
        if personaje["dinero"] <= 0:
          personaje["vida"] -= fuerza
          if personaje["vida"] <= 0:
            print("GAME OVER")
            sys.exit()
        else:
          personaje["dinero"] -= fuerza
          
          
        
      printestado()
    else:
      print("Escapaste")
      return

def entrada ():
    
  print("Te encuentras en un pasadizo oscuro y polvoriento que se adentra en la tierra. A medida\
  que caminas, la luz de la entrada se desvanece rapidamente hasta ser sólo un brillo tenue, así que\
  que te ves obligado a usar una antorcha para iluminar tu camino. A su luz parpadeante puedes ver\
  que el pasadizo se abre en seguida a una habitación. Oyes un gruñido grave, y sacas tu espada de la funda")
  print("")
  print("De repente tus ojos detectan movimiento, un montón de harapos en una esquina se levantan\
  y resulta ser un infame goblinde verrugosa piel verde, y cabezacon forma de sandia. Sus sucias\
  ropas estan cubiertas de manchas de sangre, y en una mano aún sotiene la pata asadas de una oveja\
  robada. En su otra mano lleva una espada corta de aspecto perverso.")
  print("")
  print("¡Te lanza un gruñido y carga!")
  print("")
  
  encuentro = input ("¿sacar arma/Hablar? :")
  if encuentro == "sacar arma":
   print("Sabes que el goblin es una criatura desagradable y maligna que deves matar antes de continuar")
   goblin_vida = random.randint (8,19)
   goblin_fuerza = random.randint (2,4)
   goblin(goblin_vida,goblin_fuerza)
  
  else:
     print("El goblin se abalanza sobre ti, corres embusca de la salida pero te tropiesas con las piedras el goblin salta a tu espalda y te apuñala")
     print("")
     print("Estas muerto")
      
print("\033[1m"+"LA CRIPTA DEL REY ESQUELETO"+"\033[0m")
print("---------------------------")
print("                           ")
print("Eres un valiente guerrero procedente del pueblo \
de Punta Arena, situado en la tierra de Varisia, en la costa \
del gran mar Humeante. la vida en el pueblo es sencilla pero también dura, ya que las\
tierras salvajes que lo rodean están infestadas de goblin y otros monstruos.")
print("")
print("Últimamente los monstruos se han vuelto más atrevidos, llevándose \
niños y ganado del las granjas más alejadas. Los habitantes, aterrados, han recurrido a\
ti para que les protejas. La alcaldesa, una amable mujer llamada Kendra Deverin, \
te ha prometido una recompensa de 100 piezas de oro si limpias un dungeon cercano \
donde se dice que viven tales criaturas. Es un trabajo peligroso, \
pero te notas listo para el desafio.")
print("")
print("Preparas tu equpo, una resitente armadura de cota de mallas, y una antigua espada\
larga de tu padre, y te diriges hacia el bosque, siguiendo el tosco mapa que te dio \
la alcaldesa. Tras varias horas caminando llegas a una desolada ladera. Justo por \
ensima de ti se abre la entrada oscura de un tunel.")
print("")
print("¿Qiuen quieres ser?")
opcion = input ("(airon,clair,varg,pat) :")
if opcion == "airon":
    personaje["nombre"] = "airón"
    personaje["vida"] = 13
    personaje["dinero"] = 3
    personaje["fuerza"] = 6
    personaje["xpSiguientelvl"] = 0
    personaje["xp"] = 90
    personaje["nivel"] = 1
    personaje["item"] = 0
elif opcion == "clair":
    personaje["nombre"] = "clair"
    personaje["vida"] = 16
    personaje["dinero"] = 3
    personaje["fuerza"] = 4
    personaje["xpSiguientelvl"] = 0
    personaje["xp"] = 90
    personaje["nivel"] = 1
    personaje["item"] = 0
elif opcion == "varg":
    personaje["nombre"] = "varg"
    personaje["vida"] = 12
    personaje["dinero"] = 3
    personaje["fuerza"] = 6
    personaje["xpSiguientelvl"] = 0
    personaje["xp"] = 90
    personaje["nivel"] = 1
    personaje["item"] = 0
elif opcion == "pat":
    personaje["nombre"] = "pat"
    personaje["vida"] = 17
    personaje["dinero"] = 3
    personaje["fuerza"] = 3
    personaje["xpSiguientelvl"] = 0
    personaje["xp"] = 90
    personaje["nivel"] = 1
    personaje["item"] = 0 

print(" ¡Éste debe ser el dungeon!")
print("")
print("¿Quieres armarte de valor y entrar en el tunel, ",personaje["nombre"],"?")
print("")
respuesta = input ("(si/no) :")

if respuesta == "si":
    
    print(entrada ())

else: 
  print("COBARDE!")




