# To-Do App

Aplicativo de tarefas onde o usuário consegue adicionar e alterar tarefas.

Funcionalidades principais de CRUD, criar, ler, editar e deletar uma tarefa.

## Tecnologias:
- Python
- Flask
- SQLAlchemy
- Pydantic
- Bootstrap
- HTML

## Requesitos:
Aplicação esta sendo gerenciada pelo poetry.

Se tiver rodando no linux:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Em outros ambientes pode instalar com:

```bash
pip install --user poetry
```

## Instalando o ambiente
```bash
poetry install
poetry shell
flask create-db
```
Lembrando que é necessário criar a secret key do flask para poder funcionar.
No arquivo config.py adicionar na função init_app() o código a seguir:

```python
app.config['SECRET_KEY'] = 'secret_key_de_sua_escolha'
```
E excluir a linha:
```Python
app.config.from_pyfile(".secrets.py")
```
### Executando
Tem um comando em MakeFile que já roda tudo que precisa após ativar o shell do poetry:

```bash
make run
```
Ou fazer manualmente:

```bash
export FLASK_APP=todo_app/app.py
export FLASK_DEBUG=1
flask run
```

Acessar http://localhost:5000/apidoc/swagger para ter toda a documentação da api.

// Em desenvolvimento

