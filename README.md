# Sistema Multi-Agentes para Suporte Hotmart

Sistema inteligente de atendimento ao cliente utilizando LLMs, RAG e Function Calling para responder perguntas sobre a Hotmart.

## 🏗️ Arquitetura do Sistema

O sistema é composto por 3 agentes principais:

* Agente Central: Gerencia a comunicação e roteamento das conversas
* Agente FAQ: Busca informações na base de conhecimento usando RAG
* Agente Hotmart Journey: Especialista em "Conheça a Hotmart Journey: Stars e Legacy" com acesso a dados personalizados de usuários


![Fluxo do sistema](https://raw.githubusercontent.com/vqrca/sistema-multi-agentes/main/Imagens/fluxo.png)



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

## 🔁 Como executar localmente com Docker

Este projeto foi desenvolvido para ser facilmente executado usando Docker e Docker Compose. Siga os passos abaixo para rodar a aplicação localmente:

### ✅ Pré-requisitos

- Docker instalado: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Docker Compose (já incluído nas versões atuais do Docker)

---

### 🚀 Passo a passo

#### 1. Clone o repositório

```bash
git clone https://github.com/vqrca/sistema-multi-agentes.git
cd sistema-multi-agentes
```

#### 2. Construa e execute a aplicação
```bash
docker-compose up --build
```
A aplicação será executada na porta 8501. Acesse no navegador:
http://localhost:8501


