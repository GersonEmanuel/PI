# PI - Projeto Django

Projeto Django para atividade da matéria Programação para Internet


## 1) Clone e entre no projeto

```bash
git clone https://github.com/GersonEmanuel/PI.git
cd PI
```

## 2) Crie e ative um ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3) Instale as dependencias

```bash
pip install -r requirements.txt
```

## 4) Rode as migracoes do banco de dados

```bash
python manage.py migrate
```

## 5) Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Abra no navegador:

- Inicio: http://127.0.0.1:8000/
- Sobre: http://127.0.0.1:8000/sobre/
- Admin: http://127.0.0.1:8000/admin/

## Opcional: criar usuario administrador

```bash
python manage.py createsuperuser
```

## Rotas do projeto

- `/` -> `home_view`
- `/sobre/` -> `sobre_view`
- `/admin/` -> Django admin