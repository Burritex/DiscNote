# DiscNote 📝

Envie notas diretamente do terminal para um canal do Discord via webhook, formatadas como embeds coloridos por categoria.

---

## Funcionalidades

- Digitação de nota no console com validação de entrada
- Envio automático ao Discord como embed formatado
- 3 categorias de nota com cores e títulos distintos:
  - 💡 **Nova Ideia** (amarelo)
  - 🚨 **Pendência Urgente** (vermelho)
  - 📘 **Referência/Link** (azul)
- Configuração segura via variável de ambiente (`.env`)

---

## Pré-requisitos

- Python 3.10+
- Um webhook configurado em algum canal do Discord

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Burritex/DiscNote.git
cd DiscNote
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o webhook

Crie um arquivo `.env` na raiz do projeto:

```env
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/SEU_ID/SEU_TOKEN
```

> **Como obter a URL do webhook:**  
> No Discord, acesse as configurações do canal → Integrações → Webhooks → Novo Webhook → Copiar URL do Webhook.

---

## Uso

```bash
cd src
python main.py
```

Você verá o prompt no terminal:

```
Digite a nota:
> Estudar sobre a API do Discord
Controlador: Nota enviada com sucesso ao Discord!
```

A nota aparecerá no canal do Discord como um embed:

```
💡 Nova Ideia
Estudar sobre a api do discord
Data: 12/06/2025 14:30
```

---

## Estrutura do projeto

```
DiscNote/
├── .env                          # Variáveis de ambiente (não versionar!)
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── main.py                   # Ponto de entrada
│   ├── controllers/
│   │   └── bot_controller.py     # Orquestra serviços
│   ├── models/
│   │   ├── color_enum.py         # Categorias de nota (Enum)
│   │   └── note_model.py         # Modelo de domínio Note
│   └── services/
│       ├── config_manager.py     # Leitura do .env
│       ├── note_service.py       # Criação de notas
│       └── webhook_client.py     # Comunicação com o Discord
└── tests/
    ├── test_bot_controller.py
    ├── test_color_enum.py
    ├── test_config_manager.py
    ├── test_note_model.py
    ├── test_note_service.py
    └── test_webhook_client.py
```

---

## Testes

Execute a suíte completa de testes com:

```bash
python -m pytest tests/ -v
```

Resultado esperado:

```
44 passed in 0.22s
```

---

## Arquitetura

O projeto segue um padrão de camadas simples:

```
main.py
  └─► BotController        (controllers)
        ├─► NoteService     (services) → Note (models)
        ├─► WebhookDispatcher (services)
        │     └─► ConfigManager (services)
        └─► ColorEnum       (models)
```

Cada camada tem uma responsabilidade única, facilitando testes e futuras extensões (ex: leitura de arquivo, interface gráfica).

---

## Próximas funcionalidades

- [ ] Leitura de nota a partir de arquivo de texto (`from_file`)
- [ ] Seleção interativa de categoria no console
- [ ] Suporte a múltiplos webhooks/canais

---

## Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.
