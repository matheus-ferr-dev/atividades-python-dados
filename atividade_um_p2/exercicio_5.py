# Exercício 5 - Funções matemáticas

def soma(a: int, b: int) -> int:
    return a + b

def subtracao(a: int, b: int) -> int:
    return a - b

def multiplicacao(a: int, b: int) -> int:
    negativo = (a < 0) ^ (b < 0)
    a_abs = a if a >= 0 else -a
    b_abs = b if b >= 0 else -b

    resultado = 0
    for _ in range(b_abs):
        resultado = soma(resultado, a_abs)

    return -resultado if negativo and resultado != 0 else resultado

def potencia(a: int, b: int) -> int:
    if b < 0:
        raise ValueError("Potência definida aqui apenas para expoente inteiro não negativo.")
    resultado = 1
    for _ in range(b):
        resultado = multiplicacao(resultado, a)
    return resultado

def main():
    print("=== Atividade 01 - Parte 2 (Funções) ===")
    while True:
        try:
            a = int(input("Digite o primeiro inteiro (a): "))
            b = int(input("Digite o segundo inteiro (b): "))
            break
        except ValueError:
            print("Por favor, digite apenas inteiros.")

    print("\nEscolha a operação:")
    print("1 - Soma (a + b)")
    print("2 - Subtração (a - b)")
    print("3 - Multiplicação (a * b) [via somas]")
    print("4 - Potência (a ^ b) [via multiplicações]")
    op = input("Opção: ").strip()

    try:
        if op == "1":
            print("Resultado:", soma(a, b))
        elif op == "2":
            print("Resultado:", subtracao(a, b))
        elif op == "3":
            print("Resultado:", multiplicacao(a, b))
        elif op == "4":
            print("Resultado:", potencia(a, b))
        else:
            print("Opção inválida.")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
