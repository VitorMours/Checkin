FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend

# Instalar dependências do sistema para psycopg
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Instala o netcat
RUN apt-get update \
    && apt-get install -y --no-install-recommends netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*
# Copia e instala dependências
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY ./backend .

# Copia o script wait-for-db.sh e garante permissão de execução
COPY wait-for-db.sh ./
RUN chmod +x wait-for-db.sh

# Porta exposta
ENV PORT=8001
EXPOSE 8001

# Comando padrão (mas será sobrescrito pelo docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
