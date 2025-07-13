import requests

def get_random_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Practica-Python (https://github.com/tu-usuario)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("\n🃏 Aquí tienes un chiste aleatorio:\n")
        print(f"💬 {data['joke']}\n")
    else:
        print("❌ Ocurrió un error al obtener el chiste.")

if __name__ == "__main__":
    get_random_joke()
