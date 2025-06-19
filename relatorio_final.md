# 📊 Relatório Final — Sistema Multi-Agentes para Suporte Hotmart

## 1. Introdução

Este relatório descreve os critérios de **validação**, **metrificação** e **qualidade das respostas** utilizados no sistema multi-agentes desenvolvido para atendimento inteligente na Hotmart, utilizando LLMs, RAG e Function Calling.

---

## 2. Metrificação e Validação

A validação do sistema foi conduzida com foco em dois tipos de perguntas:  
- **Perguntas informacionais gerais** (respostas via agente de FAQ)  
- **Perguntas personalizadas** sobre o programa *Hotmart Journey* (respostas via agente Journey)

### 2.1 Estratégias de avaliação

| Métrica                      | Aplicação                                                                                      |
|-----------------------------|------------------------------------------------------------------------------------------------|
| **Precisão semântica**      | Avaliada pela adequação da resposta ao conteúdo da base de conhecimento.                      |
| **Cobertura da base vetorial** | Medida pela frequência com que o sistema retorna documentos relevantes da FAISS.          |
| **Taxa de roteamento correto** | Comparação entre a decisão do agente central (`FAQ` ou `JOURNEY`) e a intenção esperada.  |
| **Taxa de acerto em testes manuais** | Foram testadas 10 perguntas; 9 foram corretamente respondidas. Acerto de **90%**. |

---

## 3. Qualidade das Respostas

### 3.1 Precisão e Relevância

As respostas são geradas a partir de dois contextos:

- **Base vetorial (FAQ)**: com embeddings semânticos criados a partir do modelo `intfloat/multilingual-e5-large`.
- **API simulada (Journey)**: retorna dados específicos com base no ID do usuário fornecido.

### 3.2 Estratégias para lidar com ambiguidade

- O sistema possui fallback: se o agente central não classifica corretamente, a pergunta é enviada ao agente de FAQ.
- A estrutura do prompt de roteamento reforça a necessidade de respostas objetivas: `"Retorne apenas 'FAQ' ou 'JOURNEY'"`.
- O uso explícito de IDs de usuário ajuda o sistema a acionar o agente correto.

### 3.3 Exemplos de comportamento esperado

| Pergunta                                     | Roteamento | Tipo de resposta                        |
|---------------------------------------------|------------|-----------------------------------------|
| "Como acessar meu e-book?"                  | FAQ        | Resposta com base na base de conhecimento |
| "Quero saber meus benefícios. ID 225"       | JOURNEY    | Resposta personalizada com dados simulados |
| "Meu ID é 000. Quais são meus ganhos?"      | JOURNEY    | Mensagem informando que o ID é inválido |

### 3.4 Limitações observadas

- Perguntas muito vagas ou fora do escopo da base podem gerar respostas genéricas.
- A classificação depende da LLM (`llama-3.3-70b-versatile`), que não é fine-tuned para esse domínio.
- A base vetorial é limitada ao conteúdo extraído da FAQ, o que restringe a cobertura.

---

## 4. Considerações finais

O sistema se mostrou funcional e coerente com os objetivos propostos, demonstrando capacidade de roteamento inteligente, resposta contextualizada e personalização.

Como próximos passos, é possível:

- Integrar métricas automáticas de similaridade semântica (e.g. cosine similarity entre vetores de embeddings);
- Medir tempo de resposta por agente;
- Implementar coleta de feedback dos usuários finais para aprimorar os prompts e classificação.

---
