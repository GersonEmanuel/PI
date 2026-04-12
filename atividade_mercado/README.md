## Requisitos

- Python 3.12+ (recomendado)
- `pip`
- Linux/macOS/Windows



## Como rodar o projeto

1. Entre na pasta do projeto:

```bash
cd atividade_mercado
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Instale as dependencias:

```bash
pip install -r requirements.txt
```

4. Rode as migracoes:

```bash
python manage.py migrate
```

5. (Opcional) Crie um usuario admin:

```bash
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

7. Acesse no navegador:

- Home Django (se configurada): `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- Lista de produtos: `http://127.0.0.1:8000/produtos/lista/`
- Detalhes de um produto: `http://127.0.0.1:8000/produtos/detalhes/<id>/`

## Configuracao atual

Arquivo principal: `mercado/settings.py`

- `DEBUG = True`
- Banco de dados: SQLite (`db.sqlite3`)
- App instalada: `produtos`
- Templates globais em `BASE_DIR / "templates"`
- Arquivos estaticos com `STATIC_URL = "static/"`


## Fluxo de dados do app produtos

- A view `lista_produtos` consulta `Produto.objects.all()` e envia o contexto `produtos` para o template.
- O template `produtos/lista_produtos.html` renderiza a lista real de produtos do banco e monta links para detalhes.
- A view `detalhes_produto` busca um produto por ID (`pk`) com `get_object_or_404`.
- O template `produtos/detalhes_produto.html` exibe `nome`, `UUID`, `preco` e `descricao` do produto.

## Modelos

No app `produtos`, existe o modelo `Produto` com os campos:

- `nome` (texto)
- `preco` (decimal)
- `descricao` (texto longo)

Para gerar novas migracoes apos alterar modelos:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Comandos uteis

Executar testes:

```bash
python manage.py test
```

Abrir shell Django:

```bash
python manage.py shell
```

Coletar estaticos (mais usado em producao):

```bash
python manage.py collectstatic
```

## Troubleshooting

- Erro de modulo Django:
  - Verifique se o ambiente virtual esta ativo.
  - Reinstale dependencias com `pip install -r requirements.txt`.

- Porta 8000 ocupada:
  - Rode em outra porta: `python manage.py runserver 8001`

- Alterou modelo e nao refletiu no banco:
  - Rode `makemigrations` e `migrate`.

## Licenca

Projeto academico/educacional.
