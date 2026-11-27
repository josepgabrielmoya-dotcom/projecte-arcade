import random
import robot


def janken():
    print("\n--- PEDRA, PAPER, TISORA ---")
    maquina = robot.robot()

    # Triar el mode de joc
    while True:
        print("1. El primer que arribi a 3 victòries")
        print("2. Al millor de 5 rondes")
        mode = input("Tria el mode de joc (1 o 2): ").strip()
        if mode == "1":
            objectiu_victories = 3
            max_rondes = None
            break
        elif mode == "2":
            objectiu_victories = 3
            max_rondes = 5
            break
        else:
            print("[Error] Tria 1 o 2.\n")

    punts_usuari = 0
    punts_robot = 0
    ronda = 1

    while True:
        print(f"\n--- Ronda {ronda} | Marcador: Tu {punts_usuari} - {punts_robot} Robot ---")
        jugada_usuari = input("Tria (pedra, paper, tisora): ").strip().lower()

        if jugada_usuari not in ["pedra", "paper", "tisora"]:
            print("[Error] Jugada no vàlida. Escriu pedra, paper o tisora.")
            continue

        jugada_robot = maquina.playing()
        print(f"El robot ha triat: {jugada_robot}")

        if jugada_usuari == jugada_robot:
            print("Empat en aquesta ronda!")
        elif (
            (jugada_usuari == "pedra" and jugada_robot == "tisora")
            or (jugada_usuari == "paper" and jugada_robot == "pedra")
            or (jugada_usuari == "tisora" and jugada_robot == "paper")
        ):
            print("Guanyes aquesta ronda!")
            punts_usuari += 1
        else:
            print("El robot guanya aquesta ronda!")
            punts_robot += 1

        # Comprovar condicions de final de partida
        if mode == "1" and (punts_usuari == objectiu_victories or punts_robot == objectiu_victories):
            break
        if mode == "2" and (punts_usuari == 3 or punts_robot == 3 or ronda == max_rondes):
            break

        ronda += 1

    # Resultat final del partit
    print("\n" + "=" * 30)
    print(f"RESULTAT FINAL: Tu {punts_usuari} - {punts_robot} Robot")
    if punts_usuari > punts_robot:
        print("Has guanyat la partida!")
    elif punts_robot > punts_usuari:
        print("El robot guanya la partida...")
    else:
        print("La partida ha acabat en empat!")
    print("=" * 30)


def nana():
    print("\n--- ENDEVINA EL NÚMERO ---")
    numero_secret = random.randint(1, 100)
    intents = 0

    print("He pensat un número entre l'1 i el 100. Intenta endevinar-lo!")

    while True:
        entrada = input("Introdueix un número: ").strip()

        if not entrada.isdigit():
            print("[Error] Si us plau, introdueix un número enter vàlid.")
            continue

        numero_usuari = int(entrada)
        intents += 1

        if numero_usuari < numero_secret:
            print("Massa baix!")
        elif numero_usuari > numero_secret:
            print("Massa alt!")
        else:
            print(f"\nFelicitats! Has encertat el número ({numero_secret}) en {intents} intents!")
            break