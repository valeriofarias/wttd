# WTTD (Welcome to the Django - Curso)

## Eventex - APP Web

Sistema de Eventos criado no curso Welcome To The Django.
Exemplo disponível em: https://eventex-valeriofarias.herokuapp.com/

Requisitos mínimos:

    git
    heroku
    python versão >= 3.5

### Como clonar e rodar o projeto na sua máquina?

1. Clone o repositório
```
git clone https://github.com/valeriofarias/wttd.git
cd wttd
```
2. Crie um ambiente virtual
```
python -m venv .venv
```
3. Ative o ambiente virtual
```
unix source .venv/bin/activate
windows .\venv\Scripts\activate
```
4. Instale as dependências. Obs.: Evite instalar localmente (psycopg2-binary==2.8.6 e gunicorn==20.0.4)
```
pip install -r requirements.txt
```
5. Configure a instância com o .env-sample
```
cp contrib/env-sample .env
```

6. Execute os testes
```
python manage.py test
```
Passados os testes com sucesso, rode o servidor
```
python manage.py runserver
```
Abra o navegador e acesso o projeto no endereço
```
localhost:8000 ou 127.0.0.1:8000
```
*sugestão: para facilitar seu desenvolvimento. usar o alias no seu perfil/terminal padrão, ex:

    unix:
        alias='python $VIRTUAL_ENV/../manage.py'

    windows:
        echo > wttd/.venv/Scripts/manage.bat
        insira no arquivo criado acima @python "%VIRTUAL_ENV%\..\manage.py" %*

### Como fazer o deploy?

Crie uma instância no heroku
```
heroku create minha_instância
```    
Defina uma SECRET_KEY para instância à partir do django shell
```            
django.core.management.utils.get_random_secret_key()
heroku config:set SECRET_KEY=copie_e_cole_do_valor_gerado_acima
```
Defina o DEBUG=False
```
heroku config:set DEBUG=False
```
Configure o serviço de email preencha os dados em .env como desejar

Envie o código para o heroku
```
git push heroku
```
