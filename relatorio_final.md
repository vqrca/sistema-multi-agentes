# 📊 Relatório Final — Sistema Multi-Agentes para Suporte Hotmart

## 1. Introdução

Este relatório apresenta a implementação e validação de um sistema multi-agentes desenvolvido para otimizar o atendimento ao cliente da Hotmart, utilizando tecnologias de Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) e Function Calling. O sistema foi projetado para fornecer respostas precisas e personalizadas, dividindo as responsabilidades entre três agentes especializados.

A primeira implementação tentou desenvolver os agentes sem etapas condicionais, permitindo que todos os agentes processassem simultaneamente as consultas. Esta abordagem apresentou limitações significativas:
**Problema Identificado:** O agente central acionava sequencialmente todos os agentes até encontrar a resposta adequada
**Impacto:** Aumento no tempo de resposta e consumo desnecessário de recursos
**Resultado:** Respostas corretas, mas com eficiência comprometida

### Solução Implementada
A arquitetura foi reformulada com base em uma estratégia de roteamento inteligente:

1. Classificação Prévia: O agente central analisa e categoriza a consulta antes do processamento

2. Roteamento Condicional: Direcionamento específico baseado na classificação:

* FAQ: Consultas gerais → Agente de Busca RAG
* Journey: Consultas sobre faturamento/programas → Agente Especialista Journey

Com isso, consegui otimizar o processo com a ativação apenas do agente necessário para cada tipo de consulta.
---

## 2. Estratégia de Validação e Metrificação

### 2.1. Tipos de Perguntas Testadas
Para validar o sistema, as perguntas foram divididas em três categorias:

**Consultas Gerais da FAQ**
> Ex: "Como mudo meu e-mail na Hotmart?"
<p align="left">
  <img src="https://github.com/user-attachments/assets/5f962762-63a3-490b-bdf1-c5f0d38fc95f"width="50%"/>

> Ex: "Quais formas de pagamento vocês aceitam?"
<p align="left">
  <img src="https://github.com/user-attachments/assets/42589d7a-f91b-46e3-9e08-cf52ce5153e8"width="50%"/>

**Consultas sobre o programa Hotmart Journey: Stars e Legacy**
> Ex:"Tenho direito ao Legacy? Já bati 10k de faturamento. Meu ID é 456"
<p align="left">
  <img src="https://github.com/user-attachments/assets/f9734326-0c16-4bf5-8d15-05bb37d95c97"width="50%"/>

> Ex: "Quais são os meus benefícios? ID 908"
<p align="left">
  <img src="https://github.com/user-attachments/assets/8002eb77-7b9d-4d0c-91e5-e6c9407b59ca"width="50%"/>

> Tentando IDs que não existem na base de dados fictícia:
<p align="left">
  <img src="https://github.com/user-attachments/assets/49f22b5a-95fe-4025-9f6c-1cdb138f60d4"width="50%"/>
</p>

**Consultas Ambíguas ou Genéricas**

> Ex: "Quero saber mais sobre a Hotmart."

<p align="left">
  <img src="https://github.com/user-attachments/assets/f43d318a-f359-4dfc-af0b-21dd90570365"width="50%"/>
</p>

> Ex: Me ajuda com benefícios da plataforma."

<p align="left">
  <img src="https://github.com/user-attachments/assets/b2b9ffab-5304-4237-ba16-f5a9c704e033"width="50%"/>
</p>

> Ex: "O que é Hotmart Journey?"
<p align="left">
  <img src="https://github.com/user-attachments/assets/f017bb0e-cd04-4d4a-b8fc-60b71d0b8ef4"width="50%"/>


## 2.2. Métricas Utilizadas
Para mensurar a qualidade das respostas, utilizei as seguintes métricas qualitativas e quantitativas:

a) Precisão do Roteamento
Avalia se a classificação feita pelo agente central foi correta:

| Tipo de Pergunta         | Nº de Testes | Roteamento Correto | Precisão (%) |
|--------------------------|--------------|---------------------|---------------|
| FAQ                      | 10           | 10                  | 100%          |
| Journey (com faturamento)| 8            | 7                   | 87,5%         |
| Ambíguas                 | 6            | 5                   | 83,3%         |

b) Relevância da Resposta
Avaliação manual baseada em critérios de completude, clareza e adequação da resposta (em escala de 1 a 5):

| Tipo de Pergunta | Média de Relevância |
|------------------|---------------------|
| FAQ              | 4,6                 |
| Journey          | 4,8                 |
| Ambíguas         | 3,9                 |

## 3. Tratamento de Ambiguidades e Complexidade

* **Ambiguidade:** Quando a pergunta é genérica, o agente central tenta extrair palavras-chave e, caso não consiga classificar com confiança, retorna com uma solicitação de refinamento:

> “Você poderia me dar mais detalhes sobre sua dúvida? Está relacionada a pagamento, benefícios ou outro assunto?”

* **Consultas Complexas:** Para perguntas longas com múltiplos tópicos, o sistema divide a questão e processa em etapas:

> Ex: “Quero saber sobre meu acesso ao Stars e também como mudar o cartão cadastrado.”
→ Primeiro, envia para o agente Journey → depois, passa para o RAG.

Observação: A queda na pontuação de perguntas ambíguas evidencia a necessidade de refinamento do classificador inicial ou de uma resposta padrão de redirecionamento com coleta ativa de contexto.

## 4. Considerações finais
O sistema se mostrou funcional e coerente com os objetivos propostos, demonstrando capacidade de roteamento inteligente, resposta contextualizada e personalização.

Como próximos passos, é possível:

* Integrar ferramentas de observabilidade como LangSmith e LangWatch para:

  - Monitorar o desempenho dos agentes (tempo de execução, fluxo de chamadas, histórico de respostas);
  
  - Avaliar a qualidade das respostas com análises manuais ou automáticas;
  
  - Identificar falhas, sessões mal roteadas e oportunidades de refino nos prompts e nos agentes;
  
* Implementar coleta de feedback dos usuários finais para aprimorar o sistema.

Essas integrações permitirão não apenas refinar a performance do sistema, como também manter um ciclo contínuo de melhoria baseado em dados reais de uso.


---
