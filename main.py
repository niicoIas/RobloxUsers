import requests
from colorama import Fore, Style
import os

URL_WEBHOOK_DISCORD = 'SEU_WEBHOOK_AQUI'
URL_IMAGEM_BOT = 'IMAGEM_DO_BOT'

def enviar_para_discord(nome_usuario):
    dados = {
        "content": f"disponivel: `{nome_usuario}`",
        "username": "roblox",
        "avatar_url": URL_IMAGEM_BOT
    }
    try:
        resposta = requests.post(URL_WEBHOOK_DISCORD, json=dados)
        if resposta.status_code != 204:
            
            pass
        else:
            print(f"{Fore.GREEN}Mensagem enviada para o Discord: {nome_usuario}{Style.RESET_ALL}")
    except Exception as erro:
        
        pass

def validar_nome(nome_usuario):
    url = f"https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={nome_usuario}"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            
            if dados['code'] == 0:
                print(f"{Fore.GREEN}O nome '{nome_usuario}' está disponível{Style.RESET_ALL}")
                with open('valid.txt', 'a') as arquivo:
                    arquivo.write(nome_usuario + '\n')
                print(f"Enviando nome para o Discord: {nome_usuario}")
                enviar_para_discord(nome_usuario)
            elif dados['code'] == 1:
                print(f"{Fore.RED}O nome '{nome_usuario}' já está em uso{Style.RESET_ALL}")
            elif dados['code'] == 2:
                print(f"{Fore.RED}O nome '{nome_usuario}' não é apropriado para o Roblox{Style.RESET_ALL}")
            elif dados['code'] == 10:
                print(f"{Fore.YELLOW}O nome '{nome_usuario}' pode conter informações privadas{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Não foi possível acessar a API do Roblox: {resposta.status_code} - {resposta.text}{Style.RESET_ALL}")
    except Exception as erro:
        print(f"{Fore.RED}Erro ao validar nome: {erro}{Style.RESET_ALL}")

def validar_nomes_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            nomes = arquivo.read().splitlines()
        for nome in nomes:
            validar_nome(nome)
    except Exception as erro:
        print(f"{Fore.RED}Erro ao ler arquivo: {erro}{Style.RESET_ALL}")

while True:
    print()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.BLUE}                    ______")
    print(f"                   <((((((\\\ ")
    print(f"                   /      . }}\ ")
    print(f"                   ;--..--._|}}")
    print(f"(\                 '--/\\--'  )")
    print(f" \\                | '-'  :'|")
    print(f"  \\               . -==- .-|")
    print(f"   \\               \\.__.'   \\--._")
    print(f"   [\\          __.--|       //  _/'--.")
    print(f"   \\ \\       .'-._ ('-----'/ __/      \\")
    print(f"    \\ \\     /   __>|      | '--.       |")
    print(f"     \\ \\   |   \\   |     /    /       /")
    print(f"      \\ '\\ /     \\  |     |  _/       /")
    print(f"       \\  \\       \\ |     | /        /")
    print(f"                ")
    print(f"{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Escolha uma opção:")
    print(f"{Fore.MAGENTA}[{Fore.RESET}1{Fore.MAGENTA}]{Fore.RESET} Digitar um nome de usuário manualmente")
    print(f"{Fore.MAGENTA}[{Fore.RESET}2{Fore.MAGENTA}]{Fore.RESET} Verificar uma lista de nomes a partir de um arquivo")
    print(f"{Fore.MAGENTA}[{Fore.RESET}0{Fore.MAGENTA}]{Fore.RESET} Sair")
    escolha = input(f"{Fore.MAGENTA}[{Fore.RESET}>{Fore.MAGENTA}]{Fore.RESET} ")
    if escolha == '1':
        nome = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Digite o nome de usuário: ")
        validar_nome(nome)
    elif escolha == '2':
        nome_arquivo = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Digite o nome do arquivo (.txt): ")
        validar_nomes_de_arquivo(nome_arquivo)
    elif escolha == '0':
        break
    else:
        print(f"{Fore.RED}Opção inválida{Style.RESET_ALL}")
