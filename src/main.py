from fichas_de_treino import gerar_ficha_com_ia

def main():
    print()
    titulo = "  🥋  TREINADOR VIRUTAL  🥋  "
    print(titulo.center(61, "-"))
    print()

    while True:
        nome = input("Por favor, informe seu nome: ").strip()
        if nome.isalpha():
            break
        else:
            print("Entrada inválida. Por favor, digite apenas letras.")

    print(f"\nOlá, {nome}! Vamos criar sua ficha de treino personalizada. Para isso, farei algumas perguntas.\n")

    while True:
        genero = input("1º - Informe seu gênero (masculino/feminino): ").strip().lower()
        if genero in ["masculino", "feminino"]:
            break
        else:
            print('Entrada inválida! Por favor, digite "masculino" ou "feminino".')

    while True:
        dias = int(input("2º - Informe quantos dias na semana você pretende treinar (1-7): "))
        if dias in [1, 2, 3, 4, 5, 6, 7]:
            break
        else:
            print("Entrada inválida! Por favor, digite um número de 1 a 7.")

    while True:
        musculo = input("3º - Qual músculo você quer dar prioridade? ").strip()
        if musculo.isalpha():
            break
        else:
            print("Entrada inválida! Por favor, digite apenas letras (ex: 'glúteos', 'peito', 'costas').")

    ficha = gerar_ficha_com_ia(genero, dias, musculo)
    titulo2 = "  💪  FICHA DE TREINO PERSONALIZADA  💪  "

    print()
    print(titulo2.center(61, "-"))
    print()

    print(ficha)

if __name__ == "__main__":
    main()
