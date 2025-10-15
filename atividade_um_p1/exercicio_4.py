# Exercício 4 - Mega-Sena – conferir pontos

def exercicio_4():
    print("\n[4] Mega-Sena – conferir pontos")
    print("   Dica: digite 6 números inteiros (ex.: 5 12 23 37 48 59)")
    sorteio = set()
    while len(sorteio) < 6:
        try:
            entrada = input(f"  Números sorteados ({len(sorteio)}/6): ").strip()
            nums = [int(x) for x in entrada.split()]
            for n in nums:
                sorteio.add(n)
                if len(sorteio) == 6:
                    break
        except ValueError:
            print("      Digite apenas inteiros.")
    jogo = set()
    while len(jogo) < 6:
        try:
            entrada = input(f"  Seus números ({len(jogo)}/6): ").strip()
            nums = [int(x) for x in entrada.split()]
            for n in nums:
                jogo.add(n)
                if len(jogo) == 6:
                    break
        except ValueError:
            print("      Digite apenas inteiros.")

    acertos = sorteio & jogo
    print(f"\nVocê fez {len(acertos)} ponto(s).")
    if acertos:
        print("Acertos:", sorted(acertos))

if __name__ == "__main__":
    exercicio_4()
