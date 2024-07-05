from estudante import Estudante
from lista_invertida import ListaInvertida

class Tela:
    def __init__(self):
        self.__lista_invertida = ListaInvertida()

    def tela_inicial(self):
        print("1 - Adicionar estudante")
        print("2 - Remover estudante")
        print("3 - Listar estudantes")
        print("4 - Listar estudantes por time")
        print("5 - Listar estudantes por cidade")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        return opcao

    def adicionar_estudante(self):
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        curso = input("Curso: ")
        cidade = input("Cidade: ")
        time = input("Time: ")
        estudante = Estudante(nome, idade, curso, cidade, time)
        self.__lista_invertida.adicionar_estudante(estudante)

    def remover_estudante(self):
        nome = input("Nome: ")
        estudante = self.__lista_invertida.estudantes[nome]
        self.__lista_invertida.remover_estudante(estudante)

    def listar_estudantes(self):
        print(self.__lista_invertida)

    def listar_estudantes_por_time(self):
        time = input("Time: ")
        estudantes = self.__lista_invertida.times[time]
        print("\n".join([str(estudante) for estudante in estudantes]))

    def listar_estudantes_por_cidade(self):
        cidade = input("Cidade: ")
        estudantes = self.__lista_invertida.cidade[cidade]
        print("\n".join([str(estudante) for estudante in estudantes]))

    def loop(self):
        while True:
            opcao = self.tela_inicial()
            if opcao == "1":
                self.adicionar_estudante()
            elif opcao == "2":
                self.remover_estudante()
            elif opcao == "3":
                self.listar_estudantes()
            elif opcao == "4":
                self.listar_estudantes_por_time()
            elif opcao == "5":
                self.listar_estudantes_por_cidade()
            elif opcao == "0":
                break
            else:
                print("Opção inválida")
    
    


