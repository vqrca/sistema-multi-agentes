from crewai.tools import tool
from vector_index import index
from mock_data import get_user_by_id

# Ferramenta para buscar conteúdo na base de conhecimento
@tool("retrieve_faq")
def retrieve_faq(question: str) -> str:
    """
    Busca conteúdo relevante na base de conhecimento da Hotmart.
    """
    query_engine = index.as_query_engine(similarity_top_k=1)
    response = query_engine.query(question)
    return str(response)


# Ferramenta para obter informações de um usuário
@tool("obter_info_usuario")
def get_user_info(user_id: str) -> str:
    """
    Retorna informações simuladas de um usuário da Hotmart, como faturamento e status no programa Journey.
   
    Args:
        user_id (str): ID do usuário para buscar informações
       
    Returns:
        str: Informações detalhadas do usuário formatadas
    """
    user = get_user_by_id(user_id)

    if not user:
        return f"Usuário com ID {user_id} não encontrado no sistema."

    # Monta resposta personalizada
    response = (
        f"INFORMAÇÕES DO USUÁRIO ID {user_id}:\n"
        f"Nome: {user['nome']}\n"
        f"Faturamento Total: R$ {user['faturamento_total']:,.2f}\n"
        f"Chapter: {user['chapter']}\n"
        f"Marco Atual: {user['marco']}\n"
        f"Benefícios: {user['beneficios']}\n"
    )
    return response