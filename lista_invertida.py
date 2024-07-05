from estudante import Estudante


class ListaInvertida:
    def __init__(self):
        self.__estudantes = {}
        self.__times = {}
        self.__cidade = {}

    @property
    def estudantes(self):
        return self.__estudantes

    @property
    def times(self):
        return self.__times

    @property
    def cidade(self):
        return self.__cidade
    

    def adicionar_estudante(self, estudante):
        self.__estudantes[estudante.nome] = estudante
        if estudante.time not in self.__times:
            self.__times[estudante.time] = []
        self.__times[estudante.time].append(estudante)
        if estudante.cidade not in self.__cidade:
            self.__cidade[estudante.cidade] = []
        self.__cidade[estudante.cidade].append(estudante)

        self.salvar_em_csv()


    def remover_estudante(self, estudante):
        del self.__estudantes[estudante.nome]
        self.__times[estudante.time].remove(estudante)
        self.__cidade[estudante.cidade].remove(estudante)

    def __str__(self):
        return "\n".join([str(estudante) for estudante in self.__estudantes.values()])