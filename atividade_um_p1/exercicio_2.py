# Exercício 2 - Busca em lista de inteiros

def exercicio_2():
    print("\n[2] Busca em lista de inteiros")
    numeros = []
    for i in range(1, 11):
        while True:
            try:
                n = int(input(f"  {i}/10 - Informe um número inteiro: "))
                numeros.append(n)
                break
            except ValueError:
                print("      Valor inválido. Tente novamente.")
    alvo = int(input("Novo número para buscar: "))
    posicoes = [i + 1 for i, v in enumerate(numeros) if v == alvo]  # 1-based
    if posicoes:
        print(f"O número {alvo} foi encontrado nas posições: {posicoes}")
    else:
        print(f"O número {alvo} não está na lista.")

if __name__ == "__main__":
    exercicio_2()
