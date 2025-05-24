import math

def bissecao(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("O método da bisseção requer que f(a) e f(b) tenham sinais opostos.")
        return None

    c = a
    iteracoes = 0
    max_iteracoes = 1000

    while (b - a) / 2 > tol and iteracoes < max_iteracoes:
        c = (a + b) / 2
        if f(c) == 0:
            return c 
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteracoes += 1

    if iteracoes == max_iteracoes:
        print("O método não convergiu dentro do número máximo de iterações.")
        return None

    return (a + b) / 2

# Área de parâmetros

# Defina aqui a função que você deseja encontrar a raiz
def funcao(x):
    return x**3 - x - 1

# Defina aqui o intervalo inicial [a, b]
a = 1
b = 2

# Defina aqui o criterio de parada
criterioParada = 0.1

raiz_aproximada = bissecao(funcao, a, b, criterioParada)

if raiz_aproximada is not None:
    print(f"A raiz aproximada é: {raiz_aproximada}")