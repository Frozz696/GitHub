class Player():
    def __init__(self, nombre, raza, clase, cuerpo, fuerza, constitucion,
                 movilida, agilidad, dextresa, mente, intelecto, aura,
                 xpSiguientelvl, xp, nivel, dinero, eventos, puntos_golpe,
                 defensa, iniciativa, atkcuerpoAcuerpo, atkAdistancia,
                 hechizeria, hechizoDirigido, vidamax, bolsa):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.cuerpo = cuerpo
        self.fuerza = fuerza
        self.constitucion = constitucion
        self.movilida = movilida
        self.agilidad = agilidad
        self.dextresa = dextresa
        self.mente = mente
        self.intelecto = intelecto
        self.aura = aura
        self.xpSiguientelvl = 150
        self.xp = 0
        self.nivel = 1
        self.dinero = 0
        self.evento = 0
        self.puntos_golpe = (self.cuerpo + self.constitucion + 10)
        self.defensa = (self.cuerpo + self.constitucion)
        self.iniciativa = (self.movilida + self.agilidad)
        self.atkcuerpoAcuerpo = (self.cuerpo + self.fuerza)
        self.atkAdistancia = (self.movilida + self.dextresa)
        self.hechizeria = (self.mente + self.aura)
        self.hechizoDirigido = (self.mente + self.dextresa)
        self.vidamax = self.puntos_golpe
        self.vivo = False
        self.bolsa = {}

        def curarce(self):
            self.puntos_golpe += 3
            if self.puntos_golpe > self.vidamax:
                self.puntos_golpe = self.vidamax


class Enemigo():
    def __init__(self, nombre, cuerpo, fuerza, constitucion, movilida,
                 agilidad, dextresa, mente, intelecto, aura, puntos_golpe,
                 defensa, iniciativa, atkcuerpoAcuerpo, atkAdistancia,
                 hechizeria, hechizoDirigido, vidamax, daxp, daOro):
        self.nombre = nombre
        self.cuerpo = cuerpo
        self.fuerza = fuerza
        self.constitucion = constitucion
        self.movilida = movilida
        self.agilidad = agilidad
        self.dextresa = dextresa
        self.mente = mente
        self.intelecto = intelecto
        self.aura = aura
        self.puntos_golpe = (self.cuerpo + self.constitucion + 10)
        self.defensa = (self.cuerpo + self.constitucion)
        self.iniciativa = (self.movilida + self.agilidad)
        self.atkcuerpoAcuerpo = (self.cuerpo + self.fuerza)
        self.atkAdistancia = (self.movilida + self.dextresa)
        self.hechizeria = (self.mente + self.aura)
        self.hechizoDirigido = (self.mente + self.dextresa)
        self.vidamax = self.puntos_golpe
        self.daxp = daxp
        self.daOro = daOro
        self.vivo = True


class Rata(Enemigo):
    def __init__(self, ):
        super().__init__("Rata", 2, 1, 0, 4, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 10, 2)


class Esqueleto(Enemigo):
    def __init__(self, ):
        super().__init__("Esqueleto", 10, 3, 2, 8, 2, 2, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 15, 5)


class Goblin(Enemigo):
    def __init__(self, ):
        super().__init__("Goblin", 5, 1, 1, 7, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 17, 6)
