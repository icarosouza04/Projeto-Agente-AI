from fichas_de_treino import gerar_ficha_local

if __name__ == "__main__":
    # Teste do fallback
    genero = input("Informe seu gênero (masculino/feminino): ")
    dias = int(input("Quantos dias por semana você pretende treinar? "))
    musculo = input("Qual o músculo que você quer dar prioridade? ")

    ficha = gerar_ficha_local(genero, dias, musculo)
    print("\nFicha de treino gerada localmente:\n")
    print(ficha)
