import time
import threading


if __name__ == "__main__":
    arquivo = "numero2.txt"
    print(f"--- Fase de Análise: {arquivo} ---")
    
    _, t_serial = executar_teste(arquivo, 1)
    
    for n in [1, 2, 4, 8, 12]:
        soma, t_p = executar_teste(arquivo, n)
        speedup = t_serial / t_p
        print(f"Threads {n:2} | Tempo: {t_p:.4f}s | Speedup: {speedup:.2f}")