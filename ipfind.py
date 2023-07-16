import socket
print("""\033[32m
 ___ ____    _____ ___ _   _ ____  
|_ _|  _ \  |  ___|_ _| \ | |  _ \ 
 | || |_) | | |_   | ||  \| | | | |
 | ||  __/  |  _|  | || |\  | |_| |
|___|_|     |_|   |___|_| \_|____/                          
""")
try:
    alvo = input('Digite o nome do site que deseja obter o endereço ip: ')
    ip = socket.gethostbyname(alvo)
    print(f' \033[31m O ip do alvo é => {ip}')
except socket.gaierror:
    print(f'\033[31mo site {alvo} nao foi encontrado')
