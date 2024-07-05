

class Estudante:
    def __init__(self, nome, idade, curso, cidade, time):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.cidade = cidade
        self.time = time
      
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def curso(self):
        return self.__curso
    
    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def time(self):
        return self.__time
    
    @time.setter
    def time(self, time):
        self.__time = time

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, {self.curso}, {self.cidade}, {self.time}"