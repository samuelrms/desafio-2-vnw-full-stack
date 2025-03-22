
# API Livros Vai Na Web 📚 + Docker 🐳

API para cadastro e listagem de livros com suporte a containerização

## Pré-requisitos ⚙️

### Opção 1 - Sem Docker

- Python 3.11+
- Git (opcional)

### Opção 2 - Com Docker

- Docker Desktop ([Windows/Mac](https://www.docker.com/products/docker-desktop/))
- Docker Compose (vem com Docker Desktop)

## 🛠️ Instalação Tradicional (Sem Docker)

Siga [as instruções anteriores](#opção-1---sem-docker) para instalação manual

## 🐳 Execução com Docker (Recomendado)

### 1. Clonar repositório

```bash
git clone https://github.com/samuelrms/desafio-2-vnw-full-stack.git livros-api
cd livros-api
```

### 2. Criar arquivo de ambiente

```bash
cp .env.example .env
```

### 3. Construir e executar

```bash
docker-compose up --build
```

### 4. Acessar a API

```bash
http://localhost:5000/
```

### Comandos úteis

| Comando | Descrição |
|---------|------------|
| `docker compose up` | Inicia os containers |
| `docker compose down` | Para e remove containers |
| `docker compose logs` | Mostra logs da aplicação |

## Estrutura do Projeto 📂

```bash
livros-api/
├── app/               # Código da aplicação
├── docker-compose.yml # Configuração Docker
├── Dockerfile         # Definição da imagem
├── .env.example       # Modelo de variáveis de ambiente
└── database.db        # Banco de dados (gerado automaticamente)
```

## Configuração de Ambiente ⚙️

### Arquivo .env

```ini
# Modo de desenvolvimento (1 = ativo, 0 = desativo)
FLASK_DEBUG=1

# URL do banco de dados
DATABASE_URL=sqlite:///database.db
```

## Testando com Docker 🔍

```bash
# Cadastrar livro
curl -X POST -H "Content-Type: application/json" -d '{
    "titulo": "Arquitetura Limpa",
    "categoria": "TI",
    "autor": "Robert C. Martin",
    "imagem_url": "http://exemplo.com/clean-arch.jpg"
}' http://localhost:5000/doar

# Listar livros
curl http://localhost:5000/livros
```

## Solução de Problemas Docker 🐛

### Erro: "Porta já em uso"

```bash
# Encerre outros containers
docker-compose down
```

### Erro: "Arquivo .env não encontrado"

```bash
cp .env.example .env
```

### Reconstruir containers

```bash
docker-compose down && docker-compose up --build
```

## Vantagens do Setup Docker ✅

1. Não precisa instalar Python localmente
2. Ambiente isolado e consistente
3. Fácil compartilhamento do projeto
4. Configuração replicável em qualquer máquina

## 🤝 Contribuição

Siga os mesmos passos anteriores, usando Docker para desenvolvimento:

```bash
docker-compose exec web bash  # Acessar container
```

---

**Escolha seu método preferido e divirta-se codando!** 🎮💻  
[Documentação Docker](https://docs.docker.com/) | [Site Vai Na Web](https://vainaweb.com.br/)

---

Feito com ❤️ por Samuel Ramos
