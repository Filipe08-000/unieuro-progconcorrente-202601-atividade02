import time
import threading
from itertools import islice

def somar_chunk(chunk):
    return sum(int(l) for l in chunk)

def desafio_bilhao(nome_arquivo, n_threads):
    soma_total = 0
    inicio = time.perf_counter()
    
    with open(nome_arquivo, 'r') as f:
        while True:
            lote = list(islice(f, 5000000))
            if not lote: break
            
            soma_total += sum(int(l) for l in lote)
            
    return soma_total, time.perf_counter() - inicio

if __name__ == "__main__":
    print("--- Executando Desafio Final: 1 Bilhão de Linhas ---")
    total, tempo = desafio_bilhao("numerogigante.txt", 12)
    print(f"Resultado: {total} | Tempo Total: {tempo:.2f}s")