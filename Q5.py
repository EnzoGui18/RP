def inverter_string(s):
    tamanho = len(s)
    resultado = ""

    # Loop de trás para frente, adicionando caracteres ao resultado
    for i in range(tamanho - 1, -1, -1):
        resultado += s[i]

    return resultado

# Exemplo de uso
string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)

print("String original:", string_original)
print("String invertida:", string_invertida)
