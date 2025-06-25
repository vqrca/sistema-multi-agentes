import streamlit as st
from main_agent_router import generate_response

# Configuração da página
st.set_page_config(
    page_title="Central de Atendimento Hotmart",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Título e descrição
st.title("🔥 Central de Atendimento")

# Bloco de informações com st.info
st.info("""
**Bem-vindo(a) à Central de Atendimento da Hotmart!**
        
Utilize a Inteligência Artificial para gerar a melhor resposta ✨
        
Você pode tirar dúvidas de duas formas:

1. **Perguntas gerais sobre a plataforma**  
   Exemplos:
   - *Como acessar o meu e-book?*
   - *Como me afiliar a um produto na Hotmart?*

2. **Consultas personalizadas sobre o programa *Hotmart Journey: Stars e Legacy***  
   Inclua seu **ID de usuário** na pergunta para obter uma resposta personalizada.  
   Exemplos:
   - *Meu ID é 00000. Qual é o meu faturamento atual?*
   - *Quais são meus benefícios no Hotmart Journey? Meu ID é 00000.*
        
 """)

# Inicializar estados da sessão
if "question" not in st.session_state:
    st.session_state.question = ""
if "response" not in st.session_state:
    st.session_state.response = ""
if "clear_clicked" not in st.session_state:
    st.session_state.clear_clicked = False

# Verificar se o botão limpar foi clicado na execução anterior
if st.session_state.clear_clicked:
    st.session_state.question = ""
    st.session_state.response = ""
    st.session_state.clear_clicked = False
    st.rerun()

# Campo de input
st.markdown("#### 🤔 Digite sua pergunta:")
current_question= st.text_input("Digite sua pergunta:",
                                value=st.session_state.question,
                                key="input_question",
                                label_visibility="collapsed",
                                placeholder="Ex: Como alterar a data de cobrança da minha assinatura?")

# Atualizar o estado da pergunta apenas se houver mudança
if current_question != st.session_state.question:
    st.session_state.question = current_question

col1, col2, col3 = st.columns([2, 0.5, 2])

with col1:
    generate = st.button("Gerar resposta", use_container_width=True)

with col2:
    st.markdown("")  # espaço entre os botões

with col3:
    clear_button = st.button("Limpar", use_container_width=True)

# Lógica dos botões
if generate:
    if st.session_state.question.strip():
        with st.spinner("Processando...🔥"):
            st.session_state.response = generate_response(st.session_state.question)
    else:
        st.warning("Digite uma pergunta antes de enviar.")

if clear_button:
    st.session_state.clear_clicked = True
    st.rerun()


# Exibir a resposta
if st.session_state.response:
    st.markdown("### ✅ Resposta")
    st.write(st.session_state.response)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>Desenvolvido por Valquíria Alencar 🤗 com Streamlit</p>
</div>
""", unsafe_allow_html=True)
