"""
Dados mockados para simulação de usuários da Hotmart Journey
"""

users_data = {
        "123": {
            "nome": "Maria Silva Santos",
            "faturamento_total": 15000.50,
            "chapter": "Earth",
            "marco": "Blueprint",
            "beneficios": "Badge na wallet + Amuleto exclusivo Blueprint + Cartão Business gratuito"
        },
        "456": {
            "nome": "João Carlos Oliveira", 
            "faturamento_total": 150000.75,
            "chapter": "Earth",
            "marco": "Build",
            "beneficios": "Badge na wallet + Quadro exclusivo Build + Cartão Business gratuito"
        },
        "789": {
            "nome": "Ana Paula Costa",
            "faturamento_total": 380000.25,
            "chapter": "Earth", 
            "marco": "Spaceship",
            "beneficios": "Badge na wallet + Cartão Business gratuito"
        },
        "234": {
            "nome": "Carlos Eduardo Lima",
            "faturamento_total": 750000.80,
            "chapter": "Earth",
            "marco": "Mission",
            "beneficios": "Badge na wallet + Cartão Business gratuito"
        },
        "345": {
            "nome": "Fernanda Rodrigues",
            "faturamento_total": 2500000.00,
            "chapter": "Milky Way",
            "marco": "BlackOne", 
            "beneficios": "Black Box + Pulseira exclusiva + Cartão Black premium gratuito"
        },
        "657": {
            "nome": "Roberto Silva Mendes",
            "faturamento_total": 12000000.50,
            "chapter": "Milky Way",
            "marco": "BlackVenus",
            "beneficios": "Black Box + Pulseira exclusiva + Cartão Black premium gratuito"
        },
        "908": {
            "nome": "Luciana Pereira Santos", 
            "faturamento_total": 150000000.00,
            "chapter": "Milky Way",
            "marco": "BlackSirius",
            "beneficios": "Black Box + Pulseira exclusiva + Cartão Black premium gratuito"
        },
        "101": {
            "nome": "Alexandre Martins",
            "faturamento_total": 300000000.00,
            "chapter": "Cosmos",
            "marco": "Cosmos I",
            "beneficios": "Space Helmet Cosmos I + Cartão Black premium gratuito + Nível máximo atingido!"
        },
        "225": {
            "nome": "Pedro Henrique Alves",
            "faturamento_total": 2500.00,
            "chapter": "Earth",
            "marco": "Project", 
            "beneficios": "Badge na wallet + Cartão Business disponível"
        },
        "887": {
            "nome": "Sofia Rodriguez",
            "faturamento_total": 85000.00,
            "chapter": "Earth",
            "marco": "Build",
            "beneficios": "Badge na wallet + Cartão Business gratuito (usuário internacional)"
        }
    }

# Função auxiliar para buscar usuário
def get_user_by_id(user_id: str) -> dict | None:
    """
    Busca um usuário pelo ID
    
    Args:
        user_id (str): ID do usuário
        
    Returns:
        dict | None: Dados do usuário ou None se não encontrado
    """
    return users_data.get(user_id)