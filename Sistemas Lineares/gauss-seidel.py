import numpy as np
from numpy import linalg

def gauss_seidel(sistema_aumentada, aprox_inicial, precisao, max_iteracoes):
    n = len(aprox_inicial)
    x = np.array(aprox_inicial, dtype=float)
    
    A = sistema_aumentada[:, :-1]
    B = sistema_aumentada[:, -1]

    x_anterior = np.copy(x)
    erro = precisao + 1.0
    
    print(f"Matriz A:\n{A}")
    print(f"Vetor B:\n{B}")
    print(f"Chute inicial (x0): {aprox_inicial}")
    print(f"Tolerância: {precisao}, Máximo de iterações: {max_iteracoes}\n")

    for iteracao in range(1, max_iteracoes + 1): 
        x_anterior = np.copy(x)

        for k in range(n):
            soma_termos = 0.0
            for j in range(n):
                if k != j:
                    soma_termos += A[k, j] * x[j]
            
            if np.isclose(A[k, k], 0): 
                raise ValueError(f"Erro: Elemento diagonal A[{k},{k}] é zero (ou muito próximo de zero). "
                                 "O método de Gauss-Seidel não pode prosseguir sem pivotamento.")
            
            x[k] = (B[k] - soma_termos) / A[k, k]
        
        erro = linalg.norm(x - x_anterior)

        print(f"Iteração {iteracao}: {np.array2string(x, formatter={'float_kind':lambda val: f'{val:.2f}'})} | Erro: {erro:<.2f}\n")

        if erro < precisao:
            print("--- Resultados Finais ---")
            print(f"Convergência atingida em {iteracao} iterações.")
            print(f"Solução final aproximada (X): {np.array2string(x, formatter={'float_kind':lambda val: f'{val:.2f}'})}")
            print(f"Erro final: {erro:.2f}")
            return x
    
    print(f"Máximo de iterações ({max_iteracoes}) atingido sem convergência.")
    print(f"Solução final aproximada (X): {np.array2string(x, formatter={'float_kind':lambda val: f'{val:.2f}'})}")
    print(f"Erro final: {erro:.2f}")
    return x

# --- Área de parâmetros
aprox_inicial = [0, 0, 0]
precisao = 0.1
max_iteracoes = 100

sistema = np.array([[9, -3, 1, 2],
                    [-2, 5, 3, -1],
                    [-1, 2, -7, 3]], dtype=float)

gauss_seidel(sistema, aprox_inicial, precisao, max_iteracoes)