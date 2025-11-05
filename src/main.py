from fichas_de_treino import gerar_ficha_com_ia

def main():
    print(f"\n{"="*28}")
    print("🥋   TREINADOR VIRUTAL   🥋")
    print(f"{"="*28}\n")

    nome = input("Por favor, informe seu nome: ")

    print(f"\nOlá, {nome}! Vamos criar sua ficha de treino personalizada. Para isso, farei apenas três perguntas...\n")

    genero = input("1º - Informe seu gênero (masculino/feminino): ")
    dias = int(input("2º - Quantos dias por semana você pretende treinar? "))
    musculo = input("3º - Qual o músculo que você quer dar prioridade? ")

    ficha = gerar_ficha_com_ia(genero, dias, musculo)
    
    print(f"\n{"="*27}")
    print(f"      FICHA DE TREINO      ")
    print(f"{"="*27}\n")
    print(ficha)

if __name__ == "__main__":
    main()
