import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
import os
import socket

# Inicializa o Colorama para cores no terminal
init(autoreset=True)

# User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
}
print("""
=========================================
🔍 SubDiscover - Desenvolvida por aash.victor
=========================================
""")

# Testa subdomínio com HTTP e HTTPS
def check_subdomain(subdomain, domain, output_file):
    protocols = ["http", "https"]
    for proto in protocols:
        url = f"{proto}://{subdomain}.{domain}"
        try:
            # Obtém o IP do subdomínio
            ip = socket.gethostbyname(f"{subdomain}.{domain}")
            response = requests.get(url, headers=headers, timeout=3)
            status = response.status_code

            # Mostra e salva apenas os resultados com status 200 ou 403
            if status == 200 or status == 403:
                color = get_status_color(status)
                msg = f"{color}[{status}] {url} (IP: {ip}){Style.RESET_ALL}"
                print(msg)
                save_result(output_file, f"[{status}] {url} (IP: {ip})")
            break  # Se HTTP deu certo, não testa HTTPS, ou vice-versa
        except requests.ConnectionError:
            continue  # Ignora se não conseguir conectar
        except requests.Timeout:
            continue  # Ignora timeout
        except Exception as e:
            continue  # Ignora outros erros

# Cores de acordo com o status
def get_status_color(status):
    if status == 200:
        return Fore.GREEN
    elif status == 403:
        return Fore.YELLOW
    else:
        return Fore.WHITE  # Não mostra outras cores para outros status

# Salva resultado no arquivo
def save_result(file_path, content):
    with open(file_path, 'a') as f:
        f.write(content + '\n')

# Função principal
def main():
    parser = argparse.ArgumentParser(description="Ferramenta de scanner de subdomínios.")
    parser.add_argument("domain", help="Domínio alvo (ex: site.com)")
    parser.add_argument("-w", "--wordlist", help="Wordlist de subdomínios", required=True)
    parser.add_argument("-s", "--simultaneous", type=int, default=10, help="Número de subdomínios simultâneos (padrão: 10)")
    parser.add_argument("-o", "--output", help="Arquivo para salvar os resultados", default="resultados.txt")
    args = parser.parse_args()

    # Limpa arquivo de saída anterior
    if os.path.exists(args.output):
        os.remove(args.output)

    # Lê a wordlist
    with open(args.wordlist, 'r') as file:
        subdomains = [line.strip() for line in file if line.strip()]

    print(f"\n[+] Iniciando scan em {args.domain} com {len(subdomains)} subdomínios\n")

    # Executa com threads
    with ThreadPoolExecutor(max_workers=args.simultaneous) as executor:
        for sub in subdomains:
            executor.submit(check_subdomain, sub, args.domain, args.output)

if __name__ == "__main__":
    main()

