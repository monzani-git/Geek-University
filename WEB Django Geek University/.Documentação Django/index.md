# Comandos Básicos para Iniciar um Projeto Django

## 1. Criar um novo projeto Django em um diretório específico
```bash
django-admin startproject caminho/pasta/projeto
```

 - Esse comando cria o projeto Django na pasta especificada.
 - Ele gera a estrutura inicial **com __init__.py**, **asgi.py**, **settings.py**, **urls.py**, **wsgi.py**, e o **manage.py**.

## 2. Criar uma nova aplicação dentro do projeto

```bash
python manage.py startapp core
```
 - Cria uma pasta chamada core com os arquivos básicos para uma aplicação Django.
 - Arquivos principais: views.py, models.py, admin.py, apps.py.

## 3. Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```
- Inicia o servidor local de desenvolvimento.
- O servidor será acessível em http://127.0.0.1:8000/ por padrão.

### 1. Estrutura Usada Atualmente

- Python/
- -  ├── __init__.py
- -  ├── settings.py
- -  ├── urls.py
- -  ├── asgi.py
- -  └── wsgi.py
- manage.py  # Fora da pasta Python

[### 1.1 init.py](./__init__.md)

### 1.1 init.py

Na maioria das vezes, o arquivo __init__.py pode ficar vazio, especialmente no contexto de um projeto Django. O Django irá tratá-lo como um arquivo de inicialização para o pacote, mas ele não precisa ter nada dentro para funcionar.

### 1.2 settings.py

## ***``1.2.1 Importação e Base_DIR``:***

O arquivo ***settings.py*** contém várias configurações importantes para o seu projeto Django

- BASE_DIR: Define o diretório raiz do seu projeto, baseado no local do arquivo settings.py. Isso é útil para construir caminhos relativos em relação ao diretório do projeto. 
- Você usará BASE_DIR para se referir a diretórios como o banco de dados ou arquivos estáticos.

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
```

### ***``1.2.2 Segurança``:***

- ***SECRET_KEY:*** Uma chave secreta usada pelo Django para criptografia e segurança. Em um ambiente de produção, você deve gerar uma chave secreta única e mantê-la segura.

- ***DEBUG:*** Quando está ***True***, o Django exibe informações detalhadas sobre erros, útil durante o desenvolvimento. Nunca deixe ***DEBUG*** ativado em produção, pois pode expor informações sensíveis.

- ***ALLOWED_HOSTS:*** Define quais domínios ou IPs são permitidos para acessar o seu site. Em produção, você deve configurar isso corretamente.

```python
SECRET_KEY = 'django-insecure-'
DEBUG = True
ALLOWED_HOSTS = []
```
### ***``1.2.3 Definiçã das Aplicações Instaladas``:***

- ***INSTALLED_APPS:*** Lista dos apps que fazem parte do seu projeto. Aqui você tem as ***apps padrão do Django*** (admin, auth, contenttypes, etc.)  
- Sempre que você adicionar novos apps ao seu projeto, você deve incluí-los nessa lista.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', # Criado no projeto Atual não padrão do Django
]

```

### ***``1.2.4 Middleware``:***

***MIDDLEWARE***: Middleware é uma camada que processa as requisições antes de chegar à view e as respostas antes de chegar ao navegador do usuário. Essa configuração contém diversos middleware que são essenciais para funcionalidades como segurança, sessões, autenticação, entre outros.

```Python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### ***``1.2.5 URLs``:***

***ROOT_URLCONF:*** Este parâmetro define onde o Django vai procurar as URLs principais do seu projeto. No seu caso, o Django procurará por ***urls.py*** dentro da pasta ***Python/***.

```python
ROOT_URLCONF = 'Python.urls'
```

### ***``1.2.6 Templates``:***

- ***TEMPLATES:*** Aqui você configura o Django para renderizar templates HTML. No caso, o Django irá procurar templates dentro de uma pasta chamada templates na raiz do projeto ou dentro dos diretórios dos apps (***APP_DIRS***).
- Você pode adicionar a pasta templates dentro da pasta do projeto para armazenar seus arquivos ***.html.***

```Python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], #Criada para buscar todos na pasta templates criada no APP core
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


### ***``1.2.7 Configuração WSGI``:***
- ***WSGI_APPLICATION:*** Define o ponto de entrada para o servidor WSGI, que é um servidor responsável por hospedar a aplicação. Esse valor geralmente não precisa ser alterado.

```python
WSGI_APPLICATION = 'Python.wsgi.application'
```

### ***``1.2.8 Banco de Dados``:***

- ***DATABASES:*** Aqui você configura o banco de dados do seu projeto. O Django, por padrão, usa o SQLite (um banco de dados leve que fica em um arquivo local). A configuração indica que o banco de dados será armazenado no arquivo ***db.sqlite3*** dentro do diretório base (***BASE_DIR***).
- Se você quiser usar outro banco de dados ***(como MySQL ou PostgreSQL)***, essa configuração precisará ser alterada.

````python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
````

### ***``1.2.9 Validação de Senhas``:***

***AUTH_PASSWORD_VALIDATORS:*** O Django vem com validações padrão para senhas, como verificar se a senha tem comprimento mínimo, se é comum, ou se contém apenas números. Você pode configurar ou adicionar novas validações de senha aqui.

````python
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

````

### ***``1.2.10 Internacionalização e Fuso Horário``:***

- ***LANGUAGE_CODE:*** Define o idioma padrão do seu projeto. No caso, está configurado para inglês (EUA). Você pode mudar para outro idioma, como ***pt-br*** para português brasileiro.
- ***TIME_ZONE:*** Define o fuso horário do projeto. Está configurado para UTC, mas você pode mudar para o seu fuso horário local, como ***America/Sao_Paulo.***
- ***USE_I18N e USE_TZ:*** Habilitam a internacionalização (suporte para vários idiomas) e o suporte a fusos horários.

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
```

### ***``1.2.11 Arquivo Estático``:***

***STATIC_URL:*** Define a URL base para arquivos estáticos (como CSS, JavaScript, imagens). Esses arquivos serão servidos para o cliente, e o Django irá procurá-los em diretórios como static/ ou em cada app.

```python
    STATIC_URL = 'static/'
```

### ***``1.2.12 Tipo de Campo Chave Primária``:***

***DEFAULT_AUTO_FIELD:*** Define o tipo de campo a ser usado para a chave primária em modelos. ***BigAutoField*** usa inteiros grandes (64-bit). Em versões anteriores do Django, usava-se o ***AutoField*** inteiros 32-bit).

```python
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

## ***1.2 O que você pode alterar***

- ***Adicionar mais apps:*** Se você criar novos apps, adicione-os à lista de INSTALLED_APPS.
- ***Alterar a configuração do banco de dados:*** Se você quiser usar PostgreSQL, MySQL, ou outro banco, você precisará alterar a configuração de ***DATABASES***.
- ***Configurar templates e estáticos:*** Verifique se os diretórios de templates e arquivos estáticos estão configurados corretamente.
- ***Configurar a segurança para produção:*** Quando for para produção, altere o SECRET_KEY, defina um valor para ***ALLOWED_HOSTS,*** e nunca deixe ***DEBUG = True*** em produção.

###
python .\manage.py makemigrations
python manage.py migrates

python manage.py createsuperuser