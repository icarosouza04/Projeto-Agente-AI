from agent import ficha_de_treino

def main():
    print("\n === GERADOR DE FICHA DE TREINO === \n")
    genero = input("Informe o gênero (masculino/feminino): ")
    dias = int(input("Quantos dias por semana você deseja treinar? "))
    musculo = input("Qual o músculo que você quer dar prioridade? ")

    ficha = ficha_de_treino(genero, dias, musculo)
    print("\n === FICHA GERADA === \n")
    print(ficha)

if __name__ == "__main__":
    main()
