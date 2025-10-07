
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

print("🪐 Bem-vindo à Caça ao Tesouro Espacial!")
print("O tesouro está escondido em algum ponto do mapa 3x3! 💎")

tabuleiro = [["⬜" for _ in range(3)] for _ in range(3)]
tesouro_linha = 1
tesouro_coluna = 2
tentativas = 5

for tentativa in range(1, tentativas + 1):
    print(f"\n🚀 Tentativa {tentativa} de {tentativas}")
    mostrar_tabuleiro(tabuleiro)

    linha = int(input("Escolha a linha (0, 1 ou 2): "))
    coluna = int(input("Escolha a coluna (0, 1 ou 2): "))

    if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
        print("❌ Posição inválida! Tente novamente dentro do mapa.")
        continue

    if tabuleiro[linha][coluna] == "X":
        print("⚠️ Você já tentou esse lugar!")
        continue

    if linha == tesouro_linha and coluna == tesouro_coluna:
        tabuleiro[linha][coluna] = "💎"
        mostrar_tabuleiro(tabuleiro)
        print("🎉 Você encontrou o tesouro espacial! Parabéns!")
        break
    else:
        tabuleiro[linha][coluna] = "X"
        print("🌌 Nada por aqui...")

else:
    print("😢 Suas tentativas acabaram!")
    print(f"O tesouro estava em ({tesouro_linha}, {tesouro_coluna}).")

mostrar_tabuleiro(tabuleiro)
print("Fim do jogo! 🌠")
