from agente import IA_DISPONIVEL
from google import genai
from tabulate import tabulate

def gerar_ficha_local(genero: str, dias_por_semana: int, musculo_preferencial: str):

    # Lista de divisões de treino
    # Estrutura para o gênero masculino
    # Estrutura de um fullbody (3 dias na semana)
    fullbody_variacao01 = { # Primeira variação de um treino fullbody
        "Grupos musculares": "Quadríceps, posterior de coxa, glúteos, dorsal, bíceps, peito, ombro e tríceps",
        "Exercícios": [
                    "Agachamento livre",
                    "Stiff",
                    "Puxada alta",
                    "Rosca Scott",
                    "Crucifixo na máquina",
                    "Tríceps francês",
                    "Elevação lateral"
                ]
            }
    fullbody_variacao02 = { # Segunda variação de um treino fullbody
        "Grupos musculares": "Quadríceps, posterior de coxa, glúteos, dorsal, bíceps, peito, ombro e tríceps",
        "Exercícios": [
                    "Cadeira extensora",
                    "Mesa flexora",
                    "Remada na máquina",
                    "Rosca inclinada 45º",
                    "Supino inclinado 45º",
                    "Tríceps pulley",
                    "Elevação frontal"
                ]
            }
    fullbody_variacao03 = { # Terceira variação de um treino fullbody
        "Grupos musculares": "Quadríceps, posterior de coxa, glúteos, dorsal, bíceps, peito, ombro e tríceps",
        "Exercícios": [
                    "Leg press 45º",
                    "Cadeira flexora",
                    "Pulldown",
                    "Rosca direta",
                    "Supino reto",
                    "Tríceps testa",
                    "Remada alta"
                ]
            }
    # Estrutura de um upper/lower (4 dias na semana)
    upper_variacao01 = { # Primeira variação de um treino upper (utilizado no upper/lower)
        "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
        "Exercícios": [
                    "Crucifixo na máquina",
                    "Supino inclinado",
                    "Puxada alta",
                    "Remada fechada",
                    "Rosca Scott",
                    "Tríceps pulley",
                    "Elevação lateral"
                ]
            }
    upper_variacao02 = { # Segunda variação de um treino upper (utilizado no upper/lower)
        "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
        "Exercícios": [
                    "Supino reto",
                    "Crucifixo polia baixa",
                    "Pulldown",
                    "Remada pronada",
                    "Rosca inclinada 45º",
                    "Tríceps francês",
                    "Remada alta"
                ]
            }
    upper_variacao03 = { # Terceira variação de um treino upper (utilizado no push/pull/legs + upper/lower)
        "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
        "Exercícios": [
                    "Supino reto",
                    "Crucifixo polia baixa",
                    "Puxada alta",
                    "Remada na máquina",
                    "Rosca direta",
                    "Tríceps francês",
                    "Remada alta"
                ]
            }
    lower_variacao01 = { # Primeira variação de um treino lower (utilizado no upper/lower)
        "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
        "Exercícios": [
                    "Agachamento livre",
                    "Cadeira extensora",
                    "Stiff",
                    "Mesa flexora",
                    "Elevação pélvica",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ]
            }
    lower_variacao02 = { # Segunda variação de um treino lower (utilizado no upper/lower)
        "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
        "Exercícios": [
                    "Leg press 45º",
                    "Cadeira extensora",
                    "Levantamento terra sumô",
                    "Mesa flexora",
                    "Cadeira abdutora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas sentado"
                ]
            }
    lower_variacao03 = { # Terceira variação de um treino lower (utilizado no push/pull/legs + upper/lower)
        "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
        "Exercícios": [
                    "Leg press 45º",
                    "Cadeira extensora",
                    "Mesa flexora",
                    "Cadeira abdutora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ]
            }
    # Estrutura para um push/pull/legs x2 (6 dias na semana) ou push/pull/legs + upper/lower (5 dias na semana)
    push_variacao01 = { # Primeira variação de um treino push
        "Grupos musculares": "Dorsal, bíceps e antebraço",
        "Exercícios": [
                    "Puxada alta",
                    "Remada curvada",
                    "Pulldown",
                    "Rosca Scott",
                    "Rosca inclinada 45º",
                    "Rosca inversa"
                ]
            }
    pull_variacao01 = { # Primeira variação de um treino pull
        "Grupos musculares": "Peito, ombro e tríceps",
        "Exercícios": [
                    "Crucifixo na máquina",
                    "Supino inclinado",
                    "Paralela inclinada",
                    "Elevação frontal",
                    "Elevação lateral",
                    "Tríceps francês",
                    "Tríceps pulley"
                ]
            }
    legs_variacao01 = { # Primeira variação de um treino legs
        "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
        "Exercícios": [
                    "Agachamento livre",
                    "Cadeira extensora",
                    "Stiff",
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ]
            }
    # Estrutura para o gênero feminino
    # Estrutura quadríceps/upper/isquiotibiais x2 (6 dias na semana) ou 3 dias na semana
    quadriceps_adutores_variacao01 = { # Primeira variação de um treino de quadríceps e adutores feminino
        "Grupos musculares": "Quadríceps, adutores e panturrilhas",
        "Exercícios": [
                    "Agachamento livre",
                    "Leg press",
                    "Cadeira extensora",
                    "Agachamento búlgaro",
                    "Cadeira adutora",
                    "Agachamento sumô",
                    "Elevação de panturrilhas em pé"
                ]
            }
    isquiotibiais_gluteo_variacao01 = { # Primeira variação de um treino de isquiotibiais e glúteos feminino
                "Grupos musculares": "Posterior de coxa e glúteos",
                "Exercícios": [
                    "Cadeira flexora",
                    "Mesa flexora",
                    "Stiff",
                    "Levantamento terra sumô",
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Coice na polia"
                ]
            }
    gluteo_core_variacao01 = { # Primeira variação de um treino de glúteos e core feminino
                "Grupos musculares": "Glúteos, abdômen e lombar",
                "Exercícios": [
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Coice na polia",
                    "Extensão lombar",
                    "Abdominal supra",
                    "Abdominal infra"
                ]
            }
    isquiotibiais_core_variacao01 = { # Primeira variação de um treino de isquiotibiais e core feminino
                "Grupos musculares": "Posterior de coxa, abdômen e lombar",
                "Exercícios": [
                    "Agachamento terra sumô",
                    "Mesa flexora",
                    "Stiff",
                    "Extensão lombar",
                    "Abdominal supra",
                    "Abdominal infra"
                ]
            }
    # Estrutura upper body feminino
    upper_feminino_varicao01 = { # Primeira variação de um treino de upper feminino (utilizado caso haja apenas um dia de superiores na rotina)
        "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
        "Exercícios": [
                    "Crucifixo na máquina",
                    "Puxada alta",
                    "Remada na máquina",
                    "Rosca direta",
                    "Tríceps pulley",
                    "Elevação lateral"
                ]
            }
    upper_feminino_varicao02 = { # Segunda variação de um treino de upper feminino (utilizado caso haja mais de um dia de superiores na rotina)
        "Grupos musculares": "Peito, ombro e tríceps",
        "Exercícios": [
                    "Crucifixo na máquina",
                    "Supino inclinado",
                    "Elevação frontal",
                    "Elevação lateral",
                    "Tríceps pulley"
                ]
            }
    upper_feminino_varicao03 = { # Terceira variação de um treino de upper feminino (utilizado caso haja mais de um dia de superiores na rotina)
        "Grupos musculares": "Dorsal, bíceps e posteior de ombro",
        "Exercícios": [
                    "Puxada alta",
                    "Remada na máquina",
                    "Pulldown",
                    "Rosca direta com barra",
                    "Crucifixo inverso"
                ]
            }
    
    # Lógica para selecionar e montar a ficha de treino com base nos parâmetros fornecidos
    ficha = []

    if genero.lower() in ["masculino" or "m"]:
        if dias_por_semana <= 3:
            ficha = [fullbody_variacao01, fullbody_variacao02, fullbody_variacao03]
        elif dias_por_semana == 4:
            ficha = [upper_variacao01, lower_variacao01, upper_variacao02, lower_variacao02]
        elif dias_por_semana == 5:
            ficha = [push_variacao01, pull_variacao01, legs_variacao01, upper_variacao03, lower_variacao03]
        elif dias_por_semana >= 6:
            ficha = [push_variacao01, pull_variacao01, legs_variacao01,
                     push_variacao01, pull_variacao01, legs_variacao01]
            
    elif genero.lower() in ["feminino" or "f"]:
        if dias_por_semana <= 3:
            ficha = [quadriceps_adutores_variacao01, upper_feminino_varicao01, isquiotibiais_gluteo_variacao01]
        elif dias_por_semana == 4:
            ficha = [quadriceps_adutores_variacao01, upper_feminino_varicao01,isquiotibiais_core_variacao01, gluteo_core_variacao01]
        elif dias_por_semana == 5:
            ficha = [quadriceps_adutores_variacao01, upper_feminino_varicao02,isquiotibiais_core_variacao01,
                     upper_feminino_varicao03, gluteo_core_variacao01]
        elif dias_por_semana >= 6:
            ficha = [quadriceps_adutores_variacao01, upper_feminino_varicao01, isquiotibiais_gluteo_variacao01,
                     quadriceps_adutores_variacao01, upper_feminino_varicao03, isquiotibiais_core_variacao01]
    
    else:
        ficha = [{"Grupos musculares": "Corpo inteiro", "Exercícios": ["Agachamento", "Supino", "Remada", "Rosca direta", "Tríceps pulley"]}]

    tabela_ficha = []

    # Montar a tabela formatada utilizando a biblioteca tabulate
    for dia, treino in enumerate(ficha, start=1):
        tabela_ficha.append([
            f"Dia {dia}",
            treino["Grupos musculares"],
            "\n".join(treino["Exercícios"]),
            "3-4x8-12",
            "60-90s",
            "20 min pós treino"
        ])

    tabela_formatada = tabulate(
        tabela_ficha,
        headers=["Dia", "Grupos Musculares", "Exercícios", "Séries/Reps", "Descanso", "Cardio"],
        tablefmt="fancy_grid",
        stralign="center"
    )

    print("\nConselhos adicionais:\n")
    print("""1. Foque na progressão de carga e execução dos exercícios.
2. Tente levar o músculo à falha nas últimas repetições. Isso é essencial para a hipertrofia muscular.
3. É recomendado adicionar um ou dois dias de descanso na rotina, de preferência após dois ou três dias de treinos em sequência.
4. O descanso não precisa ser completo, pode ser um dia apenas de cardio, por exemplo.
5. A dieta é tão importante quanto o treino, então não deixe-a de lado.
6. Tenha constância.

Bom treino!
          """)
    
    return tabela_formatada


def gerar_ficha_com_ia(genero: str, dias_por_semana: int, musculo_preferencial: str):
    if IA_DISPONIVEL:
        try:
            from agente import client
            client = genai.Client()

            prompt = (
                f"""Você é um professor de educação física especializado em criar fichas de treino personalizadas.
                Com base nas informações fornecidas, elabore uma ficha de treino detalhada para o usuário.
                Utilize uma linguagem clara e motivacional, adequada para iniciantes e intermediários.

                Instruções para a resposta:
                1. Crie uma ficha de treino estruturada levando em consideração o gênero {genero}, o número de {dias_por_semana} dias por semana e o músculo preferencial:{musculo_preferencial}.
                3. Inclua exercícios que foquem no músculo {musculo_preferencial}, mas também trabalhem outros grupos musculares importantes.
                4. Para cada dia de treino, liste os grupos musculares trabalhados, os exercícios recomendados, o número de séries e repetições, o tempo de descanso entre as séries e uma sugestão de cardio pós-treino.
                5. Exiba a ficha de treino em uma tabela formatada para melhor visualização.
                    A tabela deve conter as seguintes colunas:
                    - Dia
                    - Grupos Musculares
                    - Exercícios
                    - Séries/Reps
                    - Descanso
                    - Cardio
                6. Forneça dicas adicionais de treino e motivação ao final da ficha.

                """
                .format(genero=genero, dias_por_semana=dias_por_semana, musculo_preferencial=musculo_preferencial)
            )

            resposta_com_ia = client.models.generate_content(
                model="gemini-2.5-flash",
                contents = prompt
            )
            return resposta_com_ia.text
        
        except Exception as e:
            print(f"⚠️ Erro ao gerar ficha com IA: {e}. Gerando ficha padrão...")
            return gerar_ficha_local(genero, dias_por_semana, musculo_preferencial)
    else:
        print("⚠️ IA não disponível. Gerando ficha padrão...")
        return gerar_ficha_local(genero, dias_por_semana, musculo_preferencial)
    