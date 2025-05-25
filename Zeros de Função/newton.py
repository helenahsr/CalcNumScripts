import math

def newton(f, df, x0, parada, max_iteracoes):
    x = x0
    iteracoes = 0

    while abs(f(x)) > parada and iteracoes < max_iteracoes:
        if df(x) == 0:
            print("A derivada é zero. O método de Newton não pode continuar.")
            return None
        x = x - f(x) / df(x)
        iteracoes += 1

    if iteracoes == max_iteracoes:
        print("O método não convergiu dentro do número máximo de iterações.")
        return None

    return x

# Área de parâmetros

# Defina aqui a função que você deseja encontrar a raiz
def funcao(x):
    return x**3 - math.sqrt(x) - 2 # Exemplo: encontrar a raiz quadrada de 2

# Defina aqui a derivada da função
def derivadaFuncao(x):
    return 3 * x**2 - (1/2 * math.sqrt(x))

# Defina aqui a estimativa inicial
aproximacaoInicial = 1.2

# Defina aqui o criterio de parada e o número máximo de iterações
criterioParada = 0.01
maximoIteracoes = 100

raiz_aproximada = newton(funcao, derivadaFuncao, aproximacaoInicial, criterioParada, maximoIteracoes)

if raiz_aproximada is not None:
    print(f"A raiz aproximada usando o método de Newton é: {raiz_aproximada}")