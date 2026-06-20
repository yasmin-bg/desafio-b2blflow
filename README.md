## Rodar o código

Execute o comando abaixo no terminal:

```bash
python main.py
```

## Instalação das dependências

Antes de rodar o projeto, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

## Estrutura da tabela no Supabase

A tabela deve se chamar `contatos` e conter os seguintes campos:

| Campo     | Tipo | Descrição            |
|----------|------|---------------------|
| id       | int  | identificador único |
| nome     | text | nome do contato     |
| telefone | text | código de país + número com ddd |

---

## Variáveis de ambiente (.env)

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SUPABASE_URL=sua_url_aqui
SUPABASE_KEY=sua_chave_aqui

ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
```
