# Descrição 📝 

Este projeto foi desenvolvido para xxx. A estrutura foi pensada para garantir a total reprodutibilidade e facilidade de execução através do uso de Docker.

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

# Estrutura do Projeto 📂

A estrutura de pastas e arquivos está organizada da seguinte forma para facilitar a compreensão:
```
.
├── docker-compose.yaml # Arquivo principal para orquestrar os contêineres.
├── Dockerfile          # Define a imagem Docker para a aplicação principal.
├── .env.example        # Exemplo de variáveis de ambiente.
├── src/                # Pasta contendo todo o código-fonte da aplicação.
│   ├── api/            # Módulos relacionados à API (endpoints, schemas).
│   │   └── main.py
│   ├── core/           # Lógica principal, prompts, etc.
│   └── infra/          # Scripts de infraestrutura ou configuração.
├── requirements.txt    # Dependências Python do projeto.
└── README.md           # Este arquivo.
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
