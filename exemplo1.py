import time
import threading

def somar_fatia(fatia, resultados, index):
    resultados[index] = sum(int(l) for l in fatia)

def executar_teste(nome_arquivo, n_threads):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()
    
    tamanho = len(linhas)
    chunk = tamanho // n_threads
    threads, resultados = [], [0] * n_threads

    inicio = time.perf_counter()
    for i in range(n_threads):
        fatia = linhas[i*chunk : (None if i==n_threads-1 else (i+1)*chunk)]
        t = threading.Thread(target=somar_fatia, args=(fatia, resultados, i))
        threads.append(t); t.start()
    
    for t in threads: t.join()
    return sum(resultados), time.perf_counter() - inicio

if __name__ == "__main__":
    soma, tempo = executar_teste("numero1.txt", 4) 
    print(f"Exemplo 1 - Soma: {soma} | Tempo: {tempo:.4f}s")