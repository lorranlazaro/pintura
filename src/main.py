def pintar():

    while True:

        rendimento = str(
            input("Informe o rendimento da lata de tinta ou 'sair' para encerrar: ")
            .strip()
            .lower()
        )
        if rendimento == "sair":
            print("Encerrando programa...")
            break

        largura = str(input("Informe a largura da parede: ").strip().lower())
        altura = str(input("Informe a altura da parede: ").strip().lower())

        try:
            rend = float(rendimento)
            larg = float(largura)
            alt = float(altura)
        except ValueError:
            print("Entrada inválida! Digite um numero ou 'sair' para encerrar: ")
            continue

        resultado = (larg * alt) / rend

        if resultado:
            print(
                f"Você precisa de {round(resultado, 2)} latas de tinta para poder pintar a sua medida."
            )


if __name__ == "__main__":

    pintar()
