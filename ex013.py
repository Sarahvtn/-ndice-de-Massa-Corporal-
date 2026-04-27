peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)
print(f"Seu IMC:{imc:.2f} ")

if imc < 18.5:
    print("Voçê está abaixo do peso")

elif 18.5 <= imc < 25:
    print("Voçê está no peso ideal")

elif 25 <= imc < 30:
    print("Voçê está com sobrepeso")

elif 30 <= imc < 40:
    print("Voçê está com obesidade")

else:
    print("Voçê está com obesidade mórbida")

