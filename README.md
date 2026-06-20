## 🗄️ Estrutura da tabela no Supabase

A tabela deve se chamar `contatos` e conter os seguintes campos:

| Campo     | Tipo   | Descrição            |
|----------|--------|---------------------|
| id       | int    | Identificador único |
| nome     | text   | Nome do contato     |
| telefone | text   | Número com DDD + país |

## 🔐 Variáveis de ambiente (.env)

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SUPABASE_URL=sua_url_aqui
SUPABASE_KEY=sua_chave_aqui

ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
