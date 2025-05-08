# Verificador de Nomes de Usuário Roblox

Script em Python para verificar a disponibilidade de nomes de usuário no Roblox e enviar notificações ao Discord via webhook.

---

##  Funcionalidades

- Verificação de nomes de usuário em tempo real via API do Roblox
- Entrada manual ou a partir de um arquivo `.txt`
- Notificações automáticas para um canal do Discord via webhook
- Saída organizada no terminal com cores (usando Colorama)
- Salva nomes disponíveis em `valid.txt`

---

##  Requisitos

- Python 3.7 ou superior
- Instale os pacotes necessários:

```bash
pip install requests colorama
```

---

##  Como Usar

1. Clone este repositório ou copie o script para seu projeto.
2. Edite o script e configure as seguintes variáveis:
   - `URL_WEBHOOK_DISCORD`: seu webhook do Discord
   - `URL_IMAGEM_BOT`: (opcional) URL da imagem de avatar do bot

3. Execute o script:

```bash
python nome_do_script.py
```

4. Escolha uma opção no menu:
   - `1` Digitar um nome de usuário manualmente
   - `2` Verificar uma lista de nomes de um arquivo
   - `0` Sair

---

##  Exemplo de Arquivo de Entrada

Crie um arquivo `nomes.txt` com um nome por linha:

```
usuario1
usuario2
usuario3
```

---

##  Saída

- Os nomes disponíveis serão salvos automaticamente no arquivo `valid.txt`.
- Nomes disponíveis também serão enviados ao Discord via webhook configurado.

---

##  Aviso

Este projeto é apenas para fins educacionais. O uso indevido pode violar os Termos de Serviço da Roblox ou do Discord.

---
