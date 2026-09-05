# main.py

# IMPORTANTE: Importando os módulos locais criados na mesma pasta
import unidades
import moedas

def menu():
    print("\n=== CONVERSOR MULTIUSO ===")
    print("1. Converter Temperatura")
    print("2. Converter Moedas")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = menu()
        
        if opcao == "1":
            v = float(input("Digite o valor: "))
            origem = input("De (C/F/K): ")
            destino = input("Para (C/F/K): ")
            # Usando a função do arquivo unidades.py
            res = unidades.converter_temperatura(v, origem, destino)
            print(f"Resultado: {res:.2f}")

        elif opcao == "2":
            v = float(input("Digite o valor: "))
            origem = input("Moeda de origem (ex: USD): ")
            destino = input("Moeda de destino (ex: BRL): ")
            # Usando a função do arquivo moedas.py
            res, taxa = moedas.converter_moeda(v, origem, destino)
            print(f"Resultado: {res:.2f} (Taxa: {taxa:.4f})")

        elif opcao == "0":
            print("Saindo...")
            break

if __name__ == "__main__":
    main()