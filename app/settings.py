from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$4c5l+mbhib#f-_@!m^9t47jjpu#$g3)6z7-4(4139*fz6-ni9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'affi',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',  # Deve estar aqui
            ],
        },
    },
]


WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Define a pasta onde você pode armazenar seus arquivos estáticos, se necessário
]

MEDIA_URL = '/media/'  # URL pública para acessar os arquivos
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail usa esse host
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'matheusloboprogrammer@gmail.com'
EMAIL_HOST_PASSWORD = 'czqy zagj duqt fqld'

CONTACT_EMAIL = 'matheusloboprogrammer@gmail.com'

JAZZMIN_SETTINGS = {
    # Definindo título e cabeçalho do painel
    "site_title": "Guilherme Affi",
    "site_header": "Administração",
    "site_brand": "Guilherme Affi",
    "welcome_sign": "Bem-vindo ao painel de administração!",
    
    # Definindo o tema e a aparência
    "theme": "darkly",  # Usando o tema escuro para uma aparência moderna
    "color": "#143d59",  # Cor personalizada para o cabeçalho
    "header_toggle": True,  # Exibe o menu lateral quando o cabeçalho é clicado
    "navigation_expanded": True,  # Exibe o menu lateral expandido
    "show_ui_builder": False,  # Oculta a opção de UI Builder (caso não deseje editar diretamente a interface)

    # Configuração de ícones
    "icons": {
        "affi.advogado": "fas fa-user-tie",  # Advogados
        "affi.agendamento": "fas fa-calendar-check",  # Agendamentos
        "affi.artigo": "fas fa-newspaper",  # Artigos
        "affi.contato": "fas fa-address-book",  # Contatos
        "affi.falenciarecuperacao": "fas fa-archive",  # Falência e Recuperação
        "affi.perguntafaq": "fas fa-question-circle",  # Perguntas FAQ
        "affi.requerimento": "fas fa-file-alt",  # Requerimentos
        "affi.servico": "fas fa-cogs",  # Serviços
        "affi.testemunho": "fas fa-comments",  # Testemunhos
        "auth.user": "fas fa-users",  # Users
        "auth.group": "fas fa-users-cog",  # Groups
    },

    # Seções de modelos e grupos no painel
    "groups": [
        {"name": "Gestão de Usuários", "models": ["auth.user", "auth.group"]},
        {"name": "Gestão de Advogados", "models": ["affi.advogado"]},
        {"name": "Gestão de Agendamentos", "models": ["affi.agendamento"]},
        {"name": "Gestão de Artigos", "models": ["affi.artigo"]},
        {"name": "Gestão de Contatos", "models": ["affi.contato"]},
        {"name": "Gestão de Falência e Recuperação", "models": ["affi.falenciarecuperacao"]},
        {"name": "Gestão de Perguntas FAQ", "models": ["affi.perguntafaq"]},
        {"name": "Gestão de Requerimentos", "models": ["affi.requerimento"]},
        {"name": "Gestão de Serviços", "models": ["affi.servico"]},
        {"name": "Gestão de Testemunhos", "models": ["affi.testemunho"]},
    ],

    # Configuração de links personalizados na barra superior
    "topmenu_links": [
        {"name": "Dashboard", "url": "/admin/", "icon": "fas fa-tachometer-alt"},
        {"name": "Documentação", "url": "https://django-jazzmin.readthedocs.io/", "icon": "fas fa-book"},
        {"name": "Site", "url": "/", "icon": "fas fa-external-link-alt"},  # Link direto para o site público
    ],

    # Definir links rápidos no menu lateral
    "user_menu": [
        {"name": "Perfil", "url": "/admin/auth/user/", "icon": "fas fa-user"},
        {"name": "Sair", "url": "/admin/logout/", "icon": "fas fa-sign-out-alt"},
    ],

    # Customização da interface (cores, fontes, etc.)
    "dark_mode": True,  # Habilita o modo escuro
    "layout": "fluid",  # Layout fluido, para aproveitar melhor o espaço na tela

    # Customização das tabelas
    "table_style": "striped",  # Estilo de tabela listrado para melhorar a legibilidade
    "table_autosize": True,  # Tabelas com auto-ajuste de largura
}