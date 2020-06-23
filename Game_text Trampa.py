import random

personaje={}

Equipo = {"Armadura":"Cota de mallas","Arma":"Antigua espada larga"}

def entrada2():
  print ("Etrada")
  print ("El pasadizo oriental esta lleno de telarañas y parece q no se ha usado desde mucho tiempo")
  print ("")
  print ("el pasadizo occidental huele a paja y moho, pero esta limpio de telarañas")
  creaLootbox()
  direc = input ("(pasadizos oriental/pasadizo occidental) :")
  if direc == "pasadizo oriental":

    pasillo_oriental()
  elif direc == "pasadizo occidental":
    pasillo_occidental()

def trampa():
  print ("Viendo que no hay monstruos en la habitación, avanzas hacia las escaleras mientras vas recogiendo monedas")
  print ("por el camino. A media habitación tu pie se engancha en un alambre oculto y de repente un chorro de llamas")
  print ("sa disparado de la boca del demonio, ¡directamente hacia ti!")
  daño_trampa = random.randint(2,6)
  personaje["vida"] -= daño_trampa
  if vida <= 0: 
   print("Ruedas para apagar las llamas pero finalmente terminas envuelto en ellas")
   print("Estas muerto")
  printestado()

def escalera():
  print("las escaleras llevan hacia abajo")

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
    escaleras()
  elif direc == "regresar":
    entrada2()  



def pasillo_occidental():
  print("")
  print ("Huele a paja y moho")
  print ("El olor a moho se hace más fuerte a medida que te internas en el pasillo. Tras unos metros")
  print("termina en una puerta sencilla de madera, que esta semi abierta a la siguiente habitación")
  print ("")
  opcion = input ("(entrar/regresar) :")
  if opcion == "regresar":
    entrada2()


def printestado():
 print("vida: ",personaje["vida"],"dinero: ",personaje["dinero"])


def goblin (vida,fuerza):
  print ("¡tiene",(vida),"puntos de vida!")
  while vida > 0:
    accion = input("¿atacar,correr? :")
    print("Al goblin le quedan",(vida),"puntos de vida")
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
    else:
      print("El goblin ataca!!")
      print ("Corres despavorido")
      entrada2()

def creaLootbox ():
  loot = random.randint(1,5)
  if loot % 2 == 0:
    loot_vida = random.randint(1,10)
    loot_fuerza = random.randint(1,3)
    lootbox(loot_vida,loot_fuerza)

def lootbox (vida, fuerza):
  print("¡Una Lootbox salvaje apareció!")
  print("¡Tiene",vida,"puntos de vida!")
  while vida > 0:
    print("")
    accion = input("¿atacar/escapar? :")
    print ("")
    if accion == "atacar":
      vida = vida - personaje["fuerza"]
      if vida <= 0:
        print("Ganaste!!!!")
        print("Tu premio es 2 monedas")
        personaje["dinero"] += 2
      else:
        print("A la Lootboox le quedan",vida,"puntos de vida")
        print("La Lootbox ataca!!!!")
        if personaje["dinero"] <= 0:
          personaje["vida"] -= fuerza
          if personaje["vida"] <= 0:
            print("GAME OVER")
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
      
print("LA CRIPTA DEL REY ESQUELETO")
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
elif opcion == "clair":
    personaje["nombre"] = "clair"
    personaje["vida"] = 16
    personaje["dinero"] = 3
    personaje["fuerza"] = 4
elif opcion == "varg":
    personaje["nombre"] = "varg"
    personaje["vida"] = 12
    personaje["dinero"] = 3
    personaje["fuerza"] = 6
elif opcion == "pat":
    personaje["nombre"] = "pat"
    personaje["vida"] = 17
    personaje["dinero"] = 3
    personaje["fuerza"] = 3
    
    
print(" ¡Éste debe ser el dungeon!")
print("")
print("¿Quieres armarte de valor y entrar en el tunel, ",personaje["nombre"],"?")
print("")
respuesta = input ("(si/no) :")

if respuesta == "si":
    
    print(entrada ())

else: 
  print("COBARDE!")
