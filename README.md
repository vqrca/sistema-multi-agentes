# Sistema Multi-Agentes para Suporte da Hotmart 🔥

Sistema inteligente de atendimento ao cliente utilizando LLMs, RAG e Function Calling para responder perguntas sobre a Hotmart.

## 🏗️ Arquitetura do Sistema

O sistema é composto por 3 agentes principais:

* **Agente Central:** Gerencia a comunicação e roteamento das conversas
* **Agente FAQ:** Busca informações na base de conhecimento usando RAG
* **Agente Hotmart Journey:** Especialista em "Conheça a Hotmart Journey: Stars e Legacy" com acesso a dados personalizados de usuários

Este sistema foi desenvolvido para simular um atendimento inteligente multi-agente usando inteligência artificial generativa. Ele identifica o tipo de pergunta feita por um usuário e direciona a consulta para o agente mais adequado.

O fluxo geral segue estes passos:

<p align="left">
  <img src="https://raw.githubusercontent.com/vqrca/sistema-multi-agentes/main/Imagens/fluxo.png" width="70%"/>
</p>

1. Usuário envia uma pergunta via interface Streamlit.

2. Um Agente Central analisa a pergunta e faz uma classificação:

    * 'FAQ': para dúvidas gerais sobre a Hotmart (ex: funcionalidades, pagamentos, configurações)

    * 'JOURNEY': para perguntas sobre o programa Hotmart Journey: Stars e Legacy (ex: benefícios, faturamento, status do usuário)

3. A pergunta é então repassada para o agente adequado:

4. O Agente FAQ consulta a base vetorial FAISS com os artigos da FAQ e retorna uma resposta clara e objetiva.

5. O Agente Journey acessa dados fictícios de usuários (com base no ID) e retorna uma resposta específica sobre o programa e seus benefícios.

6. A resposta é exibida diretamente na interface para o usuário.


## 🧰 Tecnologias utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias:

| Tecnologia | Descrição |
|------------|-----------|
| **LLM via Groq**<br>`llama-3.3-70b-versatile` | Modelo de linguagem de alta performance utilizado para interpretar perguntas, classificar rotas e gerar respostas |
| **HuggingFace Embeddings**<br>`intfloat/multilingual-e5-large` | Modelo de embeddings multilíngue utilizado para converter perguntas e documentos em vetores semânticos |
| **LlamaIndex** | Framework para conectar LLMs a fontes externas de dados e orquestrar buscas contextuais (RAG) |
| **FAISS** | Biblioteca de busca vetorial rápida e eficiente usada para construir a base de conhecimento da FAQ |
| **CrewAI** | Sistema de orquestração multi-agente para executar tarefas distribuídas entre agentes inteligentes |
| **Streamlit** | Ferramenta para criação de interfaces web rápidas e interativas, usada na prototipação do sistema |
| **Docker & Docker Compose** | Utilizados para empacotar, isolar e facilitar a execução local do ambiente de testes |


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

## 🚀 Teste online via Streamlit Cloud

Você pode acessar a aplicação diretamente, sem precisar instalar nada localmente.

👉 [Clique aqui para acessar no Streamlit Cloud](https://sistema-multi-agentes.streamlit.app)

> A aplicação está hospedada e pronta para testes com perguntas gerais e personalizadas usando IDs.

---

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

## 🧪 Testes e Reprodutibilidade

Para facilitar os testes da aplicação, este repositório inclui exemplos de perguntas que podem ser usadas tanto para dúvidas gerais quanto para consultas personalizadas com ID de usuário.

### 📂 Arquivos disponíveis

- `testes/perguntas_exemplo.txt`: contém um conjunto de perguntas prontas para copiar e colar na interface.
- `testes/abrir_app.sh`: script shell para abrir automaticamente a aplicação no navegador local (`http://localhost:8501`).

### ▶️ Como testar

1. Após executar o projeto com Docker (veja seção anterior), rode no terminal:

```bash
bash testes/abrir_app.sh
```

2. Em seguida, visualize as perguntas de teste com:
```bash
cat testes/perguntas_exemplo.txt
```

## 📄 Relatório Final
Para complementar a entrega, foi elaborado um relatório detalhado com a estratégia de validação, métricas utilizadas e uma análise da qualidade das respostas geradas pelos agentes.

👉 [Clique aqui para acessar o relatório final](https://github.com/vqrca/sistema-multi-agentes/blob/main/relatorio_final.md)

O relatório aborda como o sistema lida com perguntas ambíguas, como os agentes são avaliados com base em relevância e precisão, e apresenta sugestões para evolução futura do protótipo.

Este projeto demonstra como agentes inteligentes, combinados com LLMs e técnicas de RAG, podem ser aplicados para melhorar o suporte ao cliente de forma personalizada e escalável. A arquitetura modular permite fácil expansão para novos domínios e fluxos de atendimento.

Mais do que um protótipo funcional, esta solução propõe uma abordagem realista e reprodutível para construir sistemas conversacionais baseados em conhecimento, com atenção à qualidade, relevância e capacidade de adaptação.



