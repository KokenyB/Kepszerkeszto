import subprocess
import sys
import os

# Fájlútvonal a requirements.txt-hez (feltételezzük, hogy ugyanabban a mappában van)
REQUIREMENTS_FILE = "requirements.txt"

def install_packages():
    """
    Telepíti a függőségeket a requirements.txt fájlból a pip segítségével.
    """
    print(f"--- Függőségek Telepítése ({REQUIREMENTS_FILE}) ---")

    if not os.path.exists(REQUIREMENTS_FILE):
        print(f"HIBA: A '{REQUIREMENTS_FILE}' fájl nem található.")
        print("Ellenőrizd, hogy a fájl létezik-e, és jó helyen van-e.")
        return

    # A pip parancs összeállítása
    try:
        # Futtatjuk a 'pip install -r requirements.txt' parancsot
        process = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS_FILE],
            check=True,  # Hiba esetén kivételt dob
            capture_output=True,
            text=True
        )

        print("\n--- Telepítés Sikeresen Befejeződött! ---")
        print(process.stdout)

    except subprocess.CalledProcessError as e:
        print("\n--- HIBA TÖRTÉNT A TELEPÍTÉS SORÁN ---")
        print(f"Hibaüzenet:\n{e.stderr}")
        print("Ellenőrizd a Python környezetedet és a függőségek helyességét.")
    except FileNotFoundError:
        print("\n--- HIBA TÖRTÉNT ---")
        print("A 'pip' parancs nem található. Ellenőrizd a Python/pip telepítését.")

if __name__ == "__main__":
    install_packages()