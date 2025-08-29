"""
Django settings for project project.

Gerado por 'django-admin startproject' usando Django 5.2.5.
"""

import os
from pathlib import Path
from datetime import timedelta

# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuração básica
SECRET_KEY = 'django-insecure-w&2%wcm@qojs$ceq#@*p0l9!k(!r%-#re8_zca12(@ddnn4@*2'
DEBUG = True
ALLOWED_HOSTS = []

# App principal
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # precisa estar no topo
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"
ASGI_APPLICATION = "project.asgi.application"

# Banco de dados (SQLite por padrão)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'meudb'),        # Nome do banco de dados
        'USER': os.environ.get('POSTGRES_USER', 'user'),      # Usuário do banco de dados
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'), # Senha do banco de dados
        'HOST': os.environ.get('POSTGRES_HOST', 'db'),        # Nome do serviço do banco de dados no docker-compose
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),      # Porta padrão do PostgreSQL
    }
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internacionalização
LANGUAGE_CODE = "pt-BR"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = "static/"

# Configuração de chave primária padrão
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==========================
# Configuração customizada
# ==========================

# Modelo de usuário customizado
AUTH_USER_MODEL = "api.User"

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        
    ),
}

# Configuração do JWT (SimpleJWT)
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# CORS (para frontend separado - React, Vue, etc.)
CORS_ALLOW_ALL_ORIGINS = True  # em produção, troque para domínios específicos
