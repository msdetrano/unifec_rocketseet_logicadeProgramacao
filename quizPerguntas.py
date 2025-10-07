# 🎯 Quiz de programação

print("🎮 Bem-vindo ao Quiz do Dev! Responda e teste seus conhecimentos. 🚀")

perguntas = [
    ["Qual linguagem é usada para criar páginas web com estrutura?", "html"],
    ["Qual linguagem é conhecida pelo símbolo 🐍?", "python"],
    ["Qual comando exibe algo na tela no Python?", "print"]
]

acertos = 0

for pergunta, resposta_certa in perguntas:
    resposta = input(pergunta + " ").lower()
    if resposta == resposta_certa:
        print("✅ Certo!")
        acertos += 1
    else:
        print("❌ Errado!")

print(f"\n🏁 Você acertou {acertos} de {len(perguntas)} perguntas!")
