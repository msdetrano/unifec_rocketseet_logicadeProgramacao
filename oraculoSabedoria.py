# 🧠 Oráculo da Sabedoria Python

print("🔮 Bem-vindo ao Oráculo da Sabedoria Python!")
assunto = input("Sobre qual tema da programação você quer saber? ").lower()

match assunto:
    case "python":
        print("🐍 Python é incrível! Simples, poderosa e muito usada no mundo todo.")
    case "variáveis":
        print("📦 Variáveis guardam informações para serem usadas mais tarde no código!")
    case "funções":
        print("⚙️ Funções ajudam a organizar seu código e evitar repetição.")
    case "loops":
        print("🔁 Loops servem para repetir ações automaticamente.")
    case _:
        print("🤔 Ainda estou aprendendo sobre esse tema... mas logo saberei tudo!")
