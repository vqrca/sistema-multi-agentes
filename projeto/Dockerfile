FROM python:3.10-slim

WORKDIR /app

# Copia arquivos do projeto para o container
COPY . .

# Instala dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Exposição da porta usada pelo Streamlit
EXPOSE 8501

# Comando default (sobrescrito pelo docker-compose)
CMD ["streamlit", "run", "app.py"]
