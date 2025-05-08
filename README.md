Verificador de Nomes de Usuário Roblox
Este script em Python verifica se nomes de usuário estão disponíveis no Roblox e envia notificações para um webhook do Discord quando um nome está disponível.

Funcionalidades
Verificação em tempo real de disponibilidade de nomes de usuário no Roblox

Suporte à entrada manual ou em lote via arquivo .txt

Notificações automáticas para um webhook do Discord

Feedback colorido no terminal para fácil visualização dos resultados

Requisitos
Python 3.7+

Pacotes:

requests

colorama

Instale os pacotes necessários com:

bash
Copiar
Editar
pip install requests colorama
Como Usar
Clone o repositório ou copie o script.

Edite o script e substitua:

SEU_WEBHOOK_AQUI pelo URL do seu webhook do Discord.

IMAGEM_DO_BOT pela URL da imagem do avatar do bot (opcional).

Execute o script:

bash
Copiar
Editar
python main.py
Escolha uma opção no menu:

Digitar um nome de usuário manualmente

Verificar uma lista de nomes a partir de um arquivo .txt

Exemplo de Arquivo de Entrada
Crie um arquivo nomes.txt com um nome por linha:

nginx
Copiar
Editar
nome1
nome2
nome3
Saída
Os nomes disponíveis serão salvos em valid.txt.

As mensagens também serão enviadas para o Discord via webhook configurado.

Observações
A API do Roblox pode retornar códigos indicando nomes inadequados, já existentes ou contendo informações privadas.

Este script é apenas para fins educacionais e não deve ser utilizado para spam ou outras práticas que violem os termos do Roblox