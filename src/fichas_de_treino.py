from agente import IA_DISPONIVEL
from google import genai

def gerar_ficha_local(genero = str, dias_por_semana = int, musculo_preferencial = str):

    rotina = []

    if genero == "masculino" and dias_por_semana <= 3:
            return {
            "Dia 1 (Fullbody)": {
                "Grupos musculares": "Quadríceps, posterior de coxa, glúteos, dorsal, bíceps, peito, ombro e tríceps",
                "Exercícios": [
                    "Agachamento livre",
                    "Stiff",
                    "Puxada alta",
                    "Rosca Scott",
                    "Crucifixo na máquina",
                    "Tríceps francês",
                    "Elevação lateral"
                ],
            "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },
            "Dia 2 (Fullbody)": {
                "Grupos musculares": "Quadríceps, posterior de coxa, glúteos, dorsal, bíceps, peito, ombro e tríceps",
                "Exercícios": [
                    "Cadeira extensora",
                    "Mesa flexora",
                    "Remada na máquina",
                    "Rosca inclinada 45º",
                    "Supino inclinado 45º",
                    "Tríceps pulley",
                    "Elevação frontal"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },
            "Dia 3 (Fullbody)": {
                "Grupos musculares": "Quadríceps, posterior de coxa, glúteos, dorsal, bíceps, peito, ombro e tríceps",
                "Exercícios": [
                    "Leg press 45º",
                    "Elevação pélvica",
                    "Pulldown",
                    "Rosca direta",
                    "Supino reto",
                    "Tríceps testa",
                    "Remada alta"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
                }
            }
        

    elif genero.lower() == "masculino" and dias_por_semana == 4:
        return {
            "Dia 1 (Superior)": {
                "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
                "Exercícios": [
                    "Crucifixo na máquina",
                    "Supino inclinado",
                    "Puxada alta",
                    "Remada na máquina",
                    "Rosca Scott",
                    "Tríceps pulley",
                    "Elevação lateral"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 2 (Inferior)": {
                "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
                "Exercícios": [
                    "Agachamento livre",
                    "Cadeira extensora",
                    "Stiff",
                    "Mesa flexora",
                    "Elevação pélvica",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 3 (Superior)": {
                "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
                "Exercícios": [
                    "Supino reto",
                    "Crucifixo polia baixa",
                    "Pulldown",
                    "Remada baixa",
                    "Rosca inclinada 45º",
                    "Tríceps francês",
                    "Remada alta"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 4 (Inferior)": {
                "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
                "Exercícios": [
                    "Leg press 45º",
                    "Cadeira extensora",
                    "Agachamento terra sumô",
                    "Mesa flexora",
                    "Cadeira abdutora",
                    "Elevação de panturrilhas sentado"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            }
        }
    

    elif genero.lower() == "masculino" and dias_por_semana == 5:
        return {
            "Dia 1 (Puxar)": {
                "Grupos musculares": "Dorsal, bíceps e antebraço",
                "Exercícios": [
                    "Puxada alta",
                    "Remada curvada",
                    "Pulldown",
                    "Rosca Scott",
                    "Rosca inclinada 45º",
                    "Rosca inversa"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 2 (Empurrar)": {
                "Grupos musculares": "Peito, ombro e tríceps",
                "Exercícios": [
                    "Crucifixo na máquina",
                    "Supino inclinado",
                    "Crucifixo polia alta",
                    "Elevação frontal",
                    "Elevação lateral",
                    "Tríceps francês",
                    "Tríceps pulley"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 3 (Pernas)": {
                "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
                "Exercícios": [
                    "Agachamento livre",
                    "Cadeira extensora",
                    "Stiff",
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 4 (Superiores)": {
                "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
                "Exercícios": [
                    "Supino reto",
                    "Crucifixo polia baixa",
                    "Puxada alta",
                    "Remada na máquina",
                    "Rosca direta",
                    "Tríceps francês",
                    "Remada alta"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 5 (Inferiores)": {
                "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
                "Exercícios": [
                    "Leg press 45º",
                    "Cadeira extensora",
                    "Mesa flexora",
                    "Cadeira abdutora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            }
        }


    elif genero.lower() == "masculino" and dias_por_semana >= 6:
        return {
            "Dia 1 (Puxar)": {
                "Grupos musculares": "Dorsal, bíceps e antebraço",
                "Exercícios": [
                    "Puxada alta",
                    "Remada na máquina",
                    "Pulldown",
                    "Rosca Scott",
                    "Rosca inclinada 45º",
                    "Rosca inversa"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 2 (Empurrar)": {
                "Grupos musculares": "Peito, ombro e tríceps",
                "Exercícios": [
                    "Crucifixo na máquina",
                    "Supino inclinado",
                    "Crucifixo polia alta",
                    "Elevação frontal",
                    "Elevação lateral",
                    "Tríceps francês",
                    "Tríceps pulley"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 3 (Pernas)": {
                "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
                "Exercícios": [
                    "Agachamento livre",
                    "Cadeira extensora",
                    "Stiff",
                    "Mesa flexora",
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 4 (Puxar 2)": {
                "Grupos musculares": "Dorsal, bíceps e antebraço",
                "Exercícios": [
                    "Puxada alta",
                    "Remada na máquina",
                    "Pulldown",
                    "Rosca Scott",
                    "Rosca inclinada 45º",
                    "Rosca inversa"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 5 (Empurrar 2)": {
                "Grupos musculares": "Peito, ombro e tríceps",
                "Exercícios": [
                    "Crucifixo na máquina",
                    "Supino inclinado",
                    "Crucifixo polia alta",
                    "Elevação frontal",
                    "Elevação lateral",
                    "Tríceps francês",
                    "Tríceps pulley"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 6 (Pernas 2)": {
                "Grupos musculares": "Quadríceps, posterior de coxa, glúteos e panturrilhas",
                "Exercícios": [
                    "Agachamento livre",
                    "Cadeira extensora",
                    "Stiff",
                    "Mesa flexora",
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            }
        }
    

    elif genero.lower() == "feminino" and dias_por_semana <= 3:
        return {
            "Dia 1 (Quadríceps e Adutores)": {
                "Grupos musculares": "Quadríceps, adutores e panturrilhas",
                "Exercícios": [
                    "Agachamento livre",
                    "Leg press",
                    "Cadeira extensora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 2 (Superiores)": {
                "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
                "Exercícios": [
                    "Crucifixo na máquina",
                    "Puxada alta",
                    "Remada na máquina",
                    "Rosca direta",
                    "Tríceps pulley",
                    "Elevação lateral"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 3 (Isquiotibiais e Glúteo)": {
                "Grupos musculares": "Posterior de coxa e glúteos",
                "Exercícios": [
                    "Agachamento terra sumô",
                    "Mesa flexora",
                    "Stiff",
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Coice na polia"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            }
        }


    elif genero.lower() == "feminino" and dias_por_semana == 4:
        return {
            "Dia 1 (Quadríceps e Adutores)": {
                "Grupos musculares": "Quadríceps, adutores e panturrilhas",
                "Exercícios": [
                    "Agachamento livre",
                    "Leg press",
                    "Cadeira extensora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 2 (Superiores)": {
                "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
                "Exercícios": [
                    "Crucifixo na máquina",
                    "Puxada alta",
                    "Remada na máquina",
                    "Rosca direta",
                    "Tríceps pulley",
                    "Elevação lateral"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 3 (Isquiotibiais e Panturrilhas)": {
                "Grupos musculares": "Posterior de coxa e panturrilhas",
                "Exercícios": [
                    "Agachamento terra sumô",
                    "Mesa flexora",
                    "Stiff",
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Coice na polia",
                    "Panturrilhas sentado",
                    "Panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 4 (Glúteo e Core)": {
                "Grupos musculares": "Glúteos, abdômen e lombar",
                "Exercícios": [
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Coice na polia",
                    "Extensão lombar",
                    "Abdominal supra",
                    "Abdominal infra"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            }
        }


    elif genero.lower() == "feminino" and dias_por_semana == 5:
        return {
            "Dia 1 (Quadríceps)": {
                "Grupos musculares": "Quadríceps, adutores e panturrilhas",
                "Exercícios": [
                    "Agachamento livre",
                    "Leg press",
                    "Cadeira extensora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 2 (Superiores - Peito, Ombro e Tríceps)": {
                "Grupos musculares": "Peito, ombro e tríceps",
                "Exercícios": [
                    "Crucifixo na máquina",
                    "Supino inclinado",
                    "Elevação frontal",
                    "Elevação lateral",
                    "Tríceps pulley"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 3 (Isquiotibiais, Abdômen e Lombar)": {
                "Grupos musculares": "Posterior de coxa, abdômen e lombar",
                "Exercícios": [
                    "Agachamento terra sumô",
                    "Mesa flexora",
                    "Stiff",
                    "Extensão lombar",
                    "Abdominal supra",
                    "Abdominal infra"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 4 (Superiores - Costas e Bíceps)": {
                "Grupos musculares": "Dorsal, bíceps e antebraço",
                "Exercícios": [
                    "Puxada alta",
                    "Remada na máquina",
                    "Pulldown",
                    "Rosca direta com barra",
                    "Rosca inversa",
                    "Crucifixo inverso"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 5 (Glúteos e Core)": {
                "Grupos musculares": "Glúteos, abdômen e lombar",
                "Exercícios": [
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Coice na polia",
                    "Extensão lombar",
                    "Abdominal supra",
                    "Abdominal infra"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            }
        }


    elif genero.lower() == "feminino" and dias_por_semana >= 6:
        return {
            "Dia 1 (Quadríceps e Adutores)": {
                "Grupos musculares": "Quadríceps, adutores e panturrilhas",
                "Exercícios": [
                    "Agachamento livre",
                    "Leg press",
                    "Cadeira extensora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 2 (Superiores)": {
                "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
                "Exercícios": [
                    "Crucifixo na máquina",
                    "Puxada alta",
                    "Remada na máquina",
                    "Rosca direta",
                    "Tríceps pulley",
                    "Elevação lateral"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 3 (Isquiotibiais e Glúteo)": {
                "Grupos musculares": "Posterior de coxa e glúteos",
                "Exercícios": [
                    "Agachamento terra sumô",
                    "Mesa flexora",
                    "Stiff",
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Coice na polia"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 4 (Quadríceps e Adutores 2)": {
                "Grupos musculares": "Quadríceps, adutores e panturrilhas",
                "Exercícios": [
                    "Agachamento livre",
                    "Leg press",
                    "Cadeira extensora",
                    "Cadeira adutora",
                    "Elevação de panturrilhas em pé"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 5 (Superiores 2)": {
                "Grupos musculares": "Dorsal, bíceps, peito, tríceps e ombro",
                "Exercícios": [
                    "Crucifixo na máquina",
                    "Puxada alta",
                    "Remada na máquina",
                    "Rosca direta",
                    "Tríceps pulley",
                    "Elevação lateral"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            },

            "Dia 6 (Isquiotibiais e Glúteo 2)": {
                "Grupos musculares": "Posterior de coxa e glúteos",
                "Exercícios": [
                    "Agachamento terra sumô",
                    "Mesa flexora",
                    "Stiff",
                    "Elevação pélvica",
                    "Cadeira abdutora",
                    "Coice na polia"
                ],
                "Séries e repetições": "3-4 séries de 8-12 repetições (carga moderada a pesada)"
            }
        }
    

    else:
            return "Desculpe, não consegui gerar uma ficha de treino com os parâmetros fornecidos. Por favor, verifique as informações e tente novamente."


def gerar_ficha_com_ia(genero: str, dias_por_semana: int, musculo_preferencial: str):
    if IA_DISPONIVEL:
        try:
            from agente import client
            client = genai.Client()

            prompt = (
                """Você é um professor de educação física especializado em criar fichas de treino personalizadas.
                Com base nas informações fornecidas, elabore uma ficha de treino detalhada.
                Gênero: {}
                Dias por semana: {}
                Músculo preferencial: {}
                A ficha deve incluir:
                - Divisão dos dias de treino
                - Grupos musculares trabalhados em cada dia
                - Lista de exercícios para cada grupo muscular
                - Séries e repetições recomendadas
                - Dias de descanso estratégicos, por exemplo, após 2 a 3 dias de treino consecutivos
                - Cardio recomendado (tipo e duração) após o treino de musculação

                Eis a estrutura de como a resposta deve ser formatada:

                Texto introdutório breve:
                Olá! Com base nas suas preferências, aqui está uma ficha de treino personalizada para você. Esta ficha é projetada para ajudar a maximizar seus ganhos no músculo {} enquanto mantém um equilíbrio saudável entre treino e recuperação.

                Divisão semanal de treino:

                Segunda-feira: Peito, Tríceps e Ombro
                Terça-feira: Costas (ênfase na espessura), Bíceps
                Quarta-feira: Pernas, Panturrilhas
                Quinta-feira: DESCANSO ATIVO ou DESCANSO TOTAL
                Sexta-feira: Ombros, Trapézio, Antebraços
                Sábado: Costas (ênfase na largura), Bíceps (leve) e Abdômen
                Domingo: DESCANSO TOTAL

                Tabela de Treino:

                | Dia             | Grupos Musculares        | Exercícios                         | Séries e Repetições       | Cardio Recomendado        |
                |-----------------|--------------------------|------------------------------------|---------------------------|---------------------------|
                | Segunda-feira   | Peito, Tríceps, Ombro    | Supino Reto, Tríceps Pulley, etc.  | 3-4 séries de 8-12 reps   | 20 min de corrida leve    |
                | Terça-feira     | Costas, Bíceps           | Puxada Alta, Rosca Direta, etc.    | 3-4 séries de 8-12 reps   | 15 min de HIIT            |
                | Quarta-feira    | Quadríceps, panturrilhas | Agachamento livre, stiff, etc      | ...                       | ...                       |
                | Quinta-feira    | Descanso completo        |                                    | ...                       | ...                       |
                
                Continue a tabela para todos os dias da semana, adaptando conforme os dias de treino e descanso.

                Conclua com uma nota motivacional:
                Lembre-se, a consistência é a chave para o sucesso no treino. Mantenha-se focado e dedicado, e você verá resultados incríveis!
                """.format(
                    genero, dias_por_semana, musculo_preferencial,musculo_preferencial
            ))

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
    