# 🛠️ Sistema de Ordens de Serviço – Django

Projeto desenvolvido com **Django** para gerenciamento de **clientes, serviços e ordens de serviço**, utilizando **SQLite** como banco de dados. Ideal para estudos, portfólio e entrevistas técnicas.

---

## 📌 Funcionalidades

* 🔐 Autenticação de usuários (login / logout)
* 👥 CRUD de Clientes
* 🧰 CRUD de Serviços
* 📄 Criação de Ordens de Serviço
* 🔗 Relacionamento entre clientes e serviços
* 🖥️ Interface com Bootstrap
* 🗃️ Banco de dados SQLite

---

## 🧱 Arquitetura do Projeto

O projeto segue o padrão MVC do Django (Model – View – Template), com separação por apps:

```
sistema_servicos/
│
├── core/            # Configurações globais, URLs principais e home
├── clientes/        # CRUD de clientes
├── servicos/        # CRUD de serviços
├── ordens/          # Ordens de serviço
├── templates/       # Templates HTML (base, login, etc)
├── venv/            # Ambiente virtual
├── manage.py
└── db.sqlite3
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Django 5.x**
* **SQLite**
* **Bootstrap 5**
* **Bootstrap Icons**

---

## 🚀 Como rodar o projeto localmente

### 1️⃣ Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd sistema_servicos
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar as dependências

```bash
pip install django
```

Ou, se existir o arquivo:

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar as migrações

```bash
python manage.py migrate
```

### 5️⃣ Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Rodar o servidor

```bash
python manage.py runserver
```

Acesse:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔐 Login

* URL: `/login/`
* Logout: `/logout/`

Algumas rotas exigem usuário autenticado.

---

## 📄 Principais Rotas

* `/clientes/` → Lista de clientes
* `/clientes/novo/` → Criar cliente
* `/servicos/` → Lista de serviços
* `/ordens/` → Ordens de serviço

---

## 🧠 Conceitos aplicados (para entrevistas)

* Separação de responsabilidades por app
* Uso correto de URLs nomeadas
* Proteção CSRF em formulários
* Uso de `get_object_or_404`
* Exclusão via método POST
* Ambiente virtual (venv)
* Boas práticas de organização Django

---

## 📸 Interface

Interface desenvolvida com **Bootstrap**, utilizando tabelas, botões de ação com ícones e formulários reutilizáveis.

---

## 📌 Melhorias futuras

* Status da ordem de serviço (Aberta / Em andamento / Finalizada)
* Cálculo automático do valor total
* Permissões por tipo de usuário
* Dashboard com métricas
* Deploy (Railway / Render)

---

## 👨‍💻 Autor

Desenvolvido por **João Vitor Moreira**
Projeto de estudo em Django com foco em backend e boas práticas.

---

⭐ Se este projeto te ajudou, deixe uma estrela no repositório!
