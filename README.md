# **Projeto - Criação de um Agente de IA**

O projeto consiste em criar um agente de IA utilizando a linguagem python.
Fui coordenado pelo professor **Renan Assunção**, meu professor da disciplina **Arquitetura e Organização de Computadores** durante o 2º período do curso de **Sistemas de Informação**.
O agente tem como objetivo gerar fichas de treino personalizadas de acordo com o perfil do usuário (gênero, dias de treino por semana e grupo muscular preferencial).
O sistema utiliza um modelo de Inteligência Artificial (IA) para criar treinos dinâmicos e individualizados.
Em caso de falha na comunicação com a IA, é acionado um fallback local, que gera fichas pré-definidas diretamente via Python.

## Funcionalidades

- Geração de fichas de treino por IA
- Fallback automático em caso de erro de conexão
- Estrutura de treinos organizados por:
    - Gênero (masculino/feminino)
    - Dias de treino (3 a 6)
    - Grupos musculares
    - Músculos preferênciais
- Entrada interativa do usuário via input()
- Saída formatada em tabela legível no terminal (usando tabulate)

## Tecnologias utilizadas

- Python 3.11+
- Ambiente virtual UV (para gerenciar o ambiente e dependências)
- Google genai (para comunicação com o modelo da Google)
- Biblioteca tabulate (para exibição organizada dos treinos)
- Biblioteca dotenv (para gerenciamento de variáveis de ambiente, como chaves de API)
