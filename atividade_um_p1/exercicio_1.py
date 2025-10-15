# Exercício 1 - Cadastro de alunos e estatísticas

def exercicio_1():
    print("\n[1] Cadastro de alunos e estatísticas")
    alunos = []
    for i in range(1, 11):
        nome = input(f"  {i}/10 - Nome do aluno: ").strip()
        while True:
            try:
                nota = float(input("      Nota (0 a 10): ").replace(",", "."))
                break
            except ValueError:
                print("      Valor inválido. Tente novamente.")
        alunos.append((nome, nota))

    # 1.2 e 1.3 - média
    mediasoma = sum(n for _, n in alunos)
    media = mediasoma / len(alunos)
    print(f"\nMédia da turma: {media:.2f}")

    # 1.4 - maior, menor e alunos correspondentes
    notas = [n for _, n in alunos]
    maior = max(notas)
    menor = min(notas)
    alunos_maior = [nome for nome, n in alunos if n == maior]
    alunos_menor = [nome for nome, n in alunos if n == menor]

    print(f"Maior nota: {maior:.2f} -> {', '.join(alunos_maior)}")
    print(f"Menor nota: {menor:.2f} -> {', '.join(alunos_menor)}")

    # 1.5 - abaixo da média
    print("\nAlunos abaixo da média:")
    abaixo = [(nome, n) for nome, n in alunos if n < media]
    if abaixo:
        for nome, n in abaixo:
            print(f"  - {nome}: {n:.2f}")
    else:
        print("  Ninguém abaixo da média.")

    # 1.6 - >= média
    print("\nAlunos com nota >= média:")
    acima_ou_igual = [(nome, n) for nome, n in alunos if n >= media]
    for nome, n in acima_ou_igual:
        print(f"  - {nome}: {n:.2f}")

if __name__ == "__main__":
    exercicio_1()
