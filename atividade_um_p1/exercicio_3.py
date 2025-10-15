# Exercício 3 - Trocar negativos por 0

def exercicio_3():
    print("\n[3] Trocar negativos por 0")
    vetor = []
    for i in range(1, 11):
        while True:
            try:
                n = int(input(f"  {i}/10 - Informe um número inteiro: "))
                vetor.append(n)
                break
            except ValueError:
                print("      Valor inválido. Tente novamente.")
    alterado = [0 if x < 0 else x for x in vetor]
    print("Resultado:", alterado)

if __name__ == "__main__":
    exercicio_3()
