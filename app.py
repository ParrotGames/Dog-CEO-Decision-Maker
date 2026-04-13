import requests
import random
import webbrowser
import time

def get_dog():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    return data["message"]

def get_decision():
    decisions = [
        "YES ✅",
        "NO ❌",
        "DO IT COWARD 😤",
        "ASK AGAIN LATER 🤔",
        "ABSOLUTELY NOT 💀",
        "NO MY BOI👦"
    ]
    return random.choice(decisions)

def main():
    print("🐶 Dog CEO Decision Maker")
    input("Press Enter to ask the Dog CEO...")

    dog_image = get_dog()
    decision = get_decision()

    print("\n📸 Dog says:")
    print(dog_image)

    print("\n🧠 Decision:")
    print(decision)

    time.sleep(2)
    webbrowser.open(dog_image)

if __name__ == "__main__":
    main()
