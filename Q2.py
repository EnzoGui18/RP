def pertence_a_fibonacci(numero):
    a, b = 0, 1

    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b

    return False

numero_informado = int(input("Informe um número: "))

if pertence_a_fibonacci(numero_informado):
    print(f"{numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"{numero_informado} não pertence à sequência de Fibonacci.")
