import socket
from threading import Thread
from queue import Queue

alvo = input("Digite o endereço IP do alvo: ")
porta_inicial = int(input("Digite a porta inicial: "))
porta_final = int(input("Digite a porta final: "))

fila_portas = Queue()

def obter_banner(s):
    """Função para obter o banner do serviço em execução na porta"""
    try:
        s.send(b'\r\n')
        banner = s.recv(1024)

        return banner.decode('utf-8', errors='ignore').strip()
    except:
        return "Serviço desconhecido (Sem Banner)"
    
def trabalhador():
    while not fila_portas.empty():
        porta = fila_portas.get()

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2.0)
            resultado = s.connect_ex((alvo, porta))

            if resultado == 0:
                banner = obter_banner(s)
                print(f"[+] Porta {porta} está ABERTA! | Banner: {banner}")
            s.close()
        
        except socket.error:
            pass

        fila_portas.task_done()

for porta in range (porta_inicial, porta_final + 1):
    fila_portas.put(porta)

numero_de_threads = 100

for _ in range(numero_de_threads):
    t = Thread(target=trabalhador)
    t.daemon = True
    t.start()    

fila_portas.join()

print("\n[V] Escaneamento e Coleta de Bannersconcluídos com sucesso!")
