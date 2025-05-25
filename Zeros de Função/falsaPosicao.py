import math

def falsa_posicao(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("O método da Falsa Posição requer que f(a) e f(b) tenham sinais opostos.")
        return None

    iteracoes = 0
    c = a 

    while iteracoes < max_iter:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(f(c)) < tol:
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iteracoes += 1

    print("O método não convergiu dentro do número máximo de iterações.")
    return None

# Área de parâmetros

# Defina aqui a função que você deseja encontrar a raiz
def funcao(x):
    return math.e**x + x

# Defina aqui o intervalo inicial [a, b]
a = -1
b = 0

# Defina aqui o criterio de parada e o número máximo de iterações
criterioParada = 0.01
maximoIteracoes = 100

raiz_aproximada = falsa_posicao(funcao, a, b, criterioParada, maximoIteracoes)

if raiz_aproximada is not None:
    print(f"A raiz aproximada usando Falsa Posição é: {raiz_aproximada}")