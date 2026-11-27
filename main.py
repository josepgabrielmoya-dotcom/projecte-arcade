import jocs

while True:
    print("\n" + "=" * 32)
    print("   BENVINGUT/DA AL MINI ARCADE")
    print("=" * 32)
    print("1. Jugar a Pedra, Paper, Tisora")
    print("2. Jugar a Endevinar el Número")
    print("S. Sortir")
    print("=" * 32)

    opcio = input("Tria una opció: ").strip().upper()

    if opcio == "1":
        jocs.janken()
    elif opcio == "2":
        jocs.nana()
    elif opcio == "S":
        print("\nGràcies per jugar al Mini Arcade! Fins aviat!")
        break
    else:
        print("\n[Error] Opció no vàlida. Si us plau, tria 1, 2 o S.")