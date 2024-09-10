# Etapa 1: Usar uma imagem base com Python
FROM python:3.9-slim

# Etapa 2: Definir o diretório de trabalho
WORKDIR /app

# Etapa 3: Copiar o arquivo de dependências
COPY requirements.txt requirements.txt

# Etapa 4: Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: Copiar o código do aplicativo
COPY . .

# Etapa 6: Expor a porta usada pelo Flask
EXPOSE 5000

# Etapa 7: Rodar o Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
