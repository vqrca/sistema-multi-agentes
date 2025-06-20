from crewai import Crew, Task
from agents import central_agent, faq_retriever, journey_agent

# Função para determinar qual agente deve responder a pergunta
def route_question(user_question, central_agent):
    """
    Função para determinar qual agente deve responder a pergunta.
    """
    routing_task = Task(
        description=f"""
        Analise a pergunta: '{user_question}'
        
        Retorne:
        - 'FAQ' se a pergunta for sobre funcionalidades gerais da Hotmart, cadastro de produtos, pagamentos, configurações básicas
        - 'JOURNEY' se a pergunta for sobre benefícios, programa Stars e Legacy, status do usuário, faturamento
        
        Seja preciso na classificação.
        """,
        expected_output="Retorne apenas 'FAQ' ou 'JOURNEY'.",
        agent=central_agent
    )
    
    crew_roteamento = Crew(
        agents=[central_agent],
        tasks=[routing_task],
        verbose=False
    )
    
    return crew_roteamento.kickoff()

# Função para perguntas de FAQ
def process_with_faq(user_question, faq_retriever):
    """
    Processa a pergunta usando o agente de FAQ.
    """
    faq_task = Task(
        description=f"Responda a esta pergunta com base na base de conhecimento da Hotmart: '{user_question}'",
        expected_output="Resposta clara, objetiva e baseada na FAQ da Hotmart.",
        agent=faq_retriever
    )
    
    crew_faq = Crew(
        agents=[faq_retriever],
        tasks=[faq_task],
        verbose=False
    )
    
    response_faq = crew_faq.kickoff()
    return response_faq.raw

# Função para perguntas de sobre Hotmart Journey
def process_with_journey(user_question, journey_agent):
    """
    Processa a pergunta usando o agente especialista em Journey.
    """
    journey_task = Task(
        description=f"""
        Analise se o usuário tem direito aos benefícios do programa Hotmart Journey: Stars e Legacy.
        Pergunta do usuário: '{user_question}'
        """,
        expected_output="Resposta personalizada com base no ID do usuário.",
        agent=journey_agent
    )
    
    crew_journey = Crew(
        agents=[journey_agent],
        tasks=[journey_task],
        verbose=False
    )
    
    response_journey = crew_journey.kickoff()
    return response_journey.raw

# Função para gerar a resposta final

def generate_response(user_question):
    decision = str(route_question(user_question, central_agent)).upper()
    
    if "JOURNEY" in decision:
        return process_with_journey(user_question, journey_agent)
    else:  # FAQ como fallback padrão
        return process_with_faq(user_question, faq_retriever)