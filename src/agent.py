from config import IA_DISPONIVEL
import google.generativeai as genai

def ficha_de_treino(genero = str, dias_por_semana = int, musculo_preferencial = str):
            
        prompt = f"""
        Você é um professor de educação física com muita experiência e especialista na criação de fichas de treino personalizadas.
        Crie uma ficha de treino detalhada para um aluno do gênero {genero} que deseja treinar com uma frequência de {dias_por_semana} dias por semana.
        O músculo que deve ter prioridade é: {musculo_preferencial}.

        A ficha deve incluir:
        - Estrutura de treino (divisão por dias)
        - Exercícios específicos para cada dia
        - Séries e repetições recomendadas
        - Tempo de descanso entre as séries
        - Cardio após musculação

        Faça a ficha em formato de tabela, com colunas na vertical para "Dia" (dia da semana), "Exercícios" (nome do exercício), "Séries" (quantidade), "Repetições" (quantidade) e "Descanso" (tempo em segundos).

        Certifique-se de que a ficha seja equilibrada, segura e adequada para o nível de condicionamento físico do aluno, promovendo progresso ao longo do tempo.
        A ficha deve promover um tempo de descando ideal para os músculos trabalhados.
        A ficha semanal deve estimular todos os grupos musculares ao longo da semana, mesmo com o foco em {musculo_preferencial}.
        Lembre-se que o genero do aluno é {genero}, a frequência de treino é {dias_por_semana} dias por semana, e o foco é no grupo muscular {musculo_preferencial}.
        """

        if IA_DISPONIVEL:
            try:
                resposta = genai.GenerativeModel("gemini-2.5-flash").generate_content(prompt)
                return resposta.text
            
            except Exception as e:
                return f"Erro ao gerar ficha com IA: {e}"
        else:
            return f"Modo offline: Ficha de treino para {genero}, {dias_por_semana} dias por semana, foco em {musculo_preferencial}."
