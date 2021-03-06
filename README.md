# Eventex 

Sistema de Eventos criado no curso Welcome to the Django.
Exemplo disponível em: https://eventex-valeriofarias.herokuapp.com/

Requisitos mínimos: git, heroku, python versão >= 3.5

## Como desenvolver

1. Clone o repositório;
2. Crie um virtualenv com Python 3.5;
3. Ative o seu virtualenv;
4. Instale as dependências;
5. Configure a instância com o .env;
6. Execute os testes.

```console
git clone https://github.com/valeriofarias/wttd.git
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test

# Para executar o app faça o seguinte:
python manage.py migrate
python manage.py runserver
# Abra o navegador em http://127.0.0.1:8000/
```

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para instância usando o script secret_gen dentro da pasta contrib feito de acordo com hbn.link/secret_gen
4. Defina DEBUG=False
5. Configure o serviço de email e preencha os dados em .env
6. Envie o código para o heroku

```console
heroku create minha instancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configure o email
git push heroku --force
```

## Como desenvolver (passo a passo detalhando o processo)

1. Clone o repositório
```
git clone https://github.com/valeriofarias/wttd.git
cd wttd
```
2. Crie um ambiente virtual
```
python -m venv .wttd
```
3. Ative o ambiente virtual
```
unix source .venv/bin/activate
windows .\venv\Scripts\activate
```
4. Instale as dependências 
Obs.: Evite instalar localmente (psycopg2-binary==2.8.6 e gunicorn==20.0.4)
```
pip install -r requirements-dev.txt
```
5. Configure a instância com o .env
```
cp contrib/env-sample .env
```

6. Execute os testes
```
python manage.py test
```
Passou nos testes, então rode as migrações e o servidor
```
python manage.py migrate
python manage.py runserver
```
Abra o navegador e acesse o projeto no endereço
```
http://localhost:8000/ ou http://127.0.0.1:8000/
```

### Dica para facilitar seu desenvolvimento: use o alias no terminal:
```
    unix:
        (.wttd)wttd$ alias manage='python $VIRTUAL_ENV/../manage.py'

    windows:
        echo > wttd/.venv/Scripts/manage.bat
        insira no arquivo criado acima @python "%VIRTUAL_ENV%\..\manage.py" %*

```

Após a configuração do alias será possível testar o app a partir de qualquer pasta dentro 
do wttd com o virtualenv ativo apenas usando:
```
manage test
```
