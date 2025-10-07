print("🔮 Bem-vindo ao jogo do número secreto!")
secreto = 8
tentativas = 0
chute = None

while chute != secreto:
    chute = int(input("Adivinhe o número (1 a 10): "))
    tentativas += 1

    if chute < secreto:
        print("📉 Muito baixo! Tente novamente.")
    elif chute > secreto:
        print("📈 Muito alto! Tente novamente.")
    else:
        print(f"🎉 Parabéns! Você acertou o número {secreto} em {tentativas} tentativas!")
