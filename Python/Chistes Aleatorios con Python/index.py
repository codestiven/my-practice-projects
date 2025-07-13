import requests

def get_random_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Python-App"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("\nAquí tienes un chiste aleatorio:\n")
        print(f"{data['joke']}\n")
    else:
        print("Ocurrió un error al obtener el chiste.")

if __name__ == "__main__":
    get_random_joke()