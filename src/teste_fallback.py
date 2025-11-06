from fichas_de_treino import gerar_ficha_local

if __name__ == "__main__":
    # Teste do fallback
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

    ficha = gerar_ficha_local(genero, dias, musculo)

    print(ficha)
