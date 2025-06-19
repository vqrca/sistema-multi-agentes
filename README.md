# Descrição 📝 

Este projeto foi desenvolvido para xxx. A estrutura foi pensada para garantir a total reprodutibilidade e facilidade de execução através do uso de Docker.

## 📁 Estrutura do Projeto

```bash
projeto/
├── Dockerfile             # Define o ambiente Docker com Streamlit
├── docker-compose.yaml    # Orquestra o container Docker e expõe a aplicação
├── .env                   # Armazena a chave de API
├── exemplos/
│   └── testes.sh          # Script para simular perguntas de FAQ e Journey via cURL
├── faiss_index/           # Arquivos da base vetorial de conhecimento (gerados com FAISS)
├── agentes.py             # Define o agente central, agente de FAQ e agente do programa Hotmart Journey
├── App.py                 # Interface com Streamlit para testar o protótipo via web
├── vector_index.py        # Carregamento dos índices da base de conhecimento com embeddings do Hugging Face
├── ferramentas.py         # Ferramentas utilizadas pelos agentes (ex: busca FAISS, API mockada)
├── main_agent_router.py   # Lógica de roteamento da pergunta, definindo qual agente será acionado
├── requirements.txt       # Dependências necessárias para rodar o projeto
└── README.md              # Documentação geral do projeto
```

# Pré-requisitos 🛠️

Antes de começar, certifique-se de que você tem as seguintes ferramentas instaladas em seu sistema:

Docker: https://www.docker.com/get-started

Docker Compose: (geralmente já vem incluído na instalação do Docker Desktop)

# Configuração ⚙️

Para configurar o projeto em seu ambiente local, siga os passos abaixo:

1. Clone o repositório:
```
git clone [URL_DO_SEU_REPOSITORIO]
cd [NOME_DA_PASTA_DO_PROJETO]
```

2. Variáveis de Ambiente (se aplicável):
   
Se o projeto utilizar um arquivo .env para gerenciar chaves de API ou outras configurações, renomeie o arquivo de exemplo e preencha com seus valores.
```
mv .env.example .env
```

Depois, edite o arquivo .env com suas credenciais.

# Executando o Projeto ▶️

O projeto é totalmente containerizado, e o docker-compose.yaml orquestra todos os serviços necessários (API, banco de dados, etc.).

Para iniciar a aplicação, execute o seguinte comando na raiz do projeto:
```
docker-compose up --build
```

O argumento --build garante que as imagens Docker serão construídas do zero na primeira vez ou caso haja alguma alteração nos arquivos de código-fonte ou no Dockerfile.

Após a execução, todos os serviços definidos no arquivo docker-compose.yaml estarão em execução e prontos para uso.

Para parar todos os contêineres, pressione Ctrl + C no terminal onde o compose está rodando, ou execute o seguinte comando em outro terminal (na mesma pasta):

```
docker-compose down
```

# Uso 🚀

Após iniciar os contêineres, a aplicação estará pronta para receber requisições.

Exemplo de Endpoint da API:

URL: http://localhost:8000/predict

Método: POST

Body (JSON):
```
{
  "prompt": "Qual é o seu prompt de teste?"
}
```
Você pode usar ferramentas como o Postman, Insomnia ou curl para interagir com a API:
```
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{"prompt": "Qual é o seu prompt de teste?"}'
```
