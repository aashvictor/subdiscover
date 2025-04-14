🔍 SubDiscover - Ferramenta Simples para Enumeração de Subdomínios

Descrição:
O SubDiscover é uma ferramenta simples e eficaz para a enumeração de subdomínios. Ela identifica subdomínios ativos com base nos códigos de resposta HTTP (como 200 ou 403) e também exibe o endereço IP correspondente de cada subdomínio encontrado.

Você pode configurar o número de requisições simultâneas, o que permite acelerar o processo de varredura — lembrando que valores mais altos tornam o scan mais rápido, mas também podem gerar mais logs nos servidores de destino.
💻 Uso:

python3 subdiscover.py -w <wordlist> -s <requisicoes_simultaneas> -o <output> <dominio>

🧪 Exemplo:

python3 subdiscover.py -w wordlist.txt -s 20 -o result.txt example.com

Parâmetros:

    -w → Arquivo contendo a wordlist de possíveis subdomínios.

    -s → Número de requisições simultâneas (quanto maior, mais rápido será o scan).

    -o → Nome do arquivo onde os resultados serão salvos.

    <dominio> → Domínio principal a ser escaneado.
