import math

# função principal
def converter_para_sistema_ponto_flutuante(B, T, M, L, numero):
    numero_normalizado_str = ''
    expoente = 0
    tamanho_numero_normalizado = ''

    if numero == 0:
        print('Zero não é um número válido')
        return

    print(f'Sistema: F({B}, {T}, {M}, {L})')

    sinal = 1 if numero < 0 else 0
    caracter_sinal = ''

    if sinal == 1:
        caracter_sinal = '-'
        numero = numero * -1 # transforma o número para positivo somente para o cálculo

    print('Sinal: negativo' if sinal == 1 else 'Sinal: positivo')
    texto_numero = str(numero)

    # separa a parte inteira e fracionária
    partes = texto_numero.split('.')
    parte_inteira = partes[0]
    parte_fracionaria = partes[1] if len(partes) > 1 else ''

    print(f'Número antes da vírgula: {parte_inteira}')
    print(f'Número depois da vírgula: {parte_fracionaria}')

    if float(parte_inteira) == 0:
        # num < 1, encontra o primeiro dígito não-nulo (não-zero) na parte fracionária
        for i, digito in enumerate(parte_fracionaria):
            if digito == '0':
                expoente += 1
            else:
                break
        
        print(f'Expoente: {-expoente}')
        # normaliza o número: m * B^0 = (n * B^e) * B^(-e)
        valor_numero_normalizado = numero * (B ** expoente)
        expoente = -expoente
        
        print(f'Número normalizado: {valor_numero_normalizado}')
        numero_normalizado_str = str(valor_numero_normalizado)
        
        # extrai os dígitos após o ponto decimal para contagem
        if '.' in numero_normalizado_str:
            tamanho_numero_normalizado = numero_normalizado_str.split('.')[1]
        else:
            tamanho_numero_normalizado = '' # seta vazio se não houver parte fracionária após normalização
        print(f'Tamanho do número normalizado: {len(tamanho_numero_normalizado)}')

    else:
        # num >= 1, expoente é o número de dígitos na parte inteira
        expoente = len(parte_inteira)
        print(f'Expoente: {expoente}')
        # Normaliza o número: m * B^0 = n * B^(-e)
        valor_numero_normalizado = numero * (B ** -expoente)
        
        print(f'Número normalizado: {valor_numero_normalizado}')
        numero_normalizado_str = str(valor_numero_normalizado)
        
        # extrai os dígitos após o ponto decimal para contagem
        if '.' in numero_normalizado_str:
            tamanho_numero_normalizado = numero_normalizado_str.split('.')[1]
        else:
            tamanho_numero_normalizado = ''
        print(f'Tamanho do número normalizado: {len(tamanho_numero_normalizado)}')

    # trata da precisão da mantissa
    t_int = int(T)
    if len(tamanho_numero_normalizado) > t_int:
        # arredondamento ou truncagem
        digitos_t = tamanho_numero_normalizado[:t_int]
        print(f'T dígitos: {digitos_t}')
        
        digito_t_mais_um = ''
        if len(tamanho_numero_normalizado) > t_int:
            digito_t_mais_um = tamanho_numero_normalizado[t_int]
        print(f'T+1 dígito: {digito_t_mais_um}')
        
        resto_t = tamanho_numero_normalizado[t_int:]
        print(f'T restante: {resto_t}')

        if digito_t_mais_um and int(digito_t_mais_um) >= 5:
            # arredonda para cima
            numero_para_somar_str = '0.'
            for i in range(t_int):
                if i == t_int - 1:
                    numero_para_somar_str += '1'
                else:
                    numero_para_somar_str += '0'
            print(f'Número a ser somado: {float(numero_para_somar_str)}')
            
            numero_normalizado_float = float(numero_normalizado_str)
            numero_normalizado_float = (numero_normalizado_float + float(numero_para_somar_str))
            numero_normalizado_str = str(numero_normalizado_float)
            
            # reavalia os dígitos após o arredondamento para a truncagem certa
            if '.' in numero_normalizado_str:
                tamanho_numero_normalizado = numero_normalizado_str.split('.')[1]
            else:
                tamanho_numero_normalizado = ''

        # trunca para T dígitos
        if '.' in numero_normalizado_str:
            partes_apos_arredondamento = numero_normalizado_str.split('.')
            parte_inteira_apos_arredondamento = partes_apos_arredondamento[0]
            parte_fracionaria_apos_arredondamento = partes_apos_arredondamento[1]
            # trunca apenas a parte fracionária
            numero_normalizado_str = parte_inteira_apos_arredondamento + '.' + parte_fracionaria_apos_arredondamento[:t_int]
        else: 
            # caso em que se tornou um inteiro, não deve ocorrer se T > 0, mas é truncado para segurança
            numero_normalizado_str = numero_normalizado_str[:t_int]

        print(f'Número normalizado após truncamento dos dígitos: {numero_normalizado_str}')

    elif len(tamanho_numero_normalizado) < t_int:
        # preenchimento com zeros
        
        digitos_t = tamanho_numero_normalizado
        print(f'T dígitos: {digitos_t}')
        
        faltantes_t = t_int - len(tamanho_numero_normalizado)
        print(f'T restante (zeros a adicionar): {faltantes_t}')
        
        # adiciona zeros para completar T dígitos
        if '.' in numero_normalizado_str:
            # já tem ponto, simplesmente adiciona zeros à parte fracionária
            partes = numero_normalizado_str.split('.')
            numero_normalizado_str = partes[0] + '.' + partes[1] + '0' * faltantes_t
        else:
            # não tem ponto, adiciona ponto e os zeros
            numero_normalizado_str += '.' + '0' * faltantes_t
            
        print(f'Número normalizado após adição de zeros: {numero_normalizado_str}')

    print(f'\nSistema: F({B}, {T}, {M}, {L})')

    # valida se ocorreu Overflow ou Underflow
    mensagem_erro = ''
    if expoente > L:
        mensagem_erro = 'Overflow!'
    elif expoente < M:
        mensagem_erro = 'Underflow!'
    
    if mensagem_erro:
        print(f'ERRO DE SISTEMA: {mensagem_erro}')
    else:
        print('Nenhum erro de overflow/underflow.')

    if sinal == 1:
        print(f'Número convertido é: {caracter_sinal}{numero_normalizado_str}*{B}^{expoente}')
    else:
        print(f'Número convertido é: {numero_normalizado_str}*{B}^{expoente}')

# função de chamada
def sistema_ponto_flutuante():
    print("\n--- Conversão para Sistema de Ponto Flutuante ---")
    
    try:
        entrada_numero = input("Digite o número a ser convertido (use '.' para decimais): ")
        if not entrada_numero:
            print('Preencha todos os campos!')
            return
        
        # Permite que o usuário use vírgula e a substitui por ponto
        numero = float(entrada_numero.replace(",", "."))

        entrada_B = input("Digite a base (B): ")
        if not entrada_B:
            print('Preencha todos os campos!')
            return
        B = float(entrada_B)

        entrada_T = input("Digite a precisão (T - número de dígitos da mantissa): ")
        if not entrada_T:
            print('Preencha todos os campos!')
            return
        T = float(entrada_T)

        entrada_M = input("Digite o expoente mínimo (M): ")
        if not entrada_M:
            print('Preencha todos os campos!')
            return
        M = float(entrada_M)

        entrada_L = input("Digite o expoente máximo (L): ")
        if not entrada_L:
            print('Preencha todos os campos!')
            return
        L = float(entrada_L)

        converter_para_sistema_ponto_flutuante(B, T, M, L, numero)

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos para todos os campos.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


sistema_ponto_flutuante()