import requests
import json

BAZAAR_API_URL = 'https://api.hypixel.net/skyblock/bazaar'

def fetch_bazaar_data():
    response = requests.get(BAZAAR_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def save_bazaar_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    try:
        print("Fetching bazaar data...")
        data = fetch_bazaar_data()
        print("Bazaar data fetched successfully.")
        
        filename = 'bazaar_data.json'
        save_bazaar_data_to_file(data, filename)
        print(f"Bazaar data saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
