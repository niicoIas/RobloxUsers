# Verificador de Nomes de Usuário Roblox

Script em Python para verificar a disponibilidade de nomes de usuário no Roblox e enviar notificações ao Discord via webhook.

---

## 🔧 Funcionalidades

- Verificação de nomes de usuário em tempo real via API do Roblox
- Entrada manual ou a partir de um arquivo `.txt`
- Notificações automáticas para um canal do Discord via webhook
- Saída organizada no terminal com cores (usando Colorama)
- Salva nomes disponíveis em `valid.txt`

---

## 📦 Requisitos

- Python 3.7 ou superior
- Instale os pacotes necessários:

```bash
pip install requests colorama
