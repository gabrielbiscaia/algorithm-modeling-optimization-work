#Definição da classe e seus métodos
class Cidade:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    #métodos get e set
    def setNome(self, nome):
        self.nome = nome

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getNome(self):
        return self.nome

    def getX(self):
        return self.x

    def getY(self):
        return self.y
